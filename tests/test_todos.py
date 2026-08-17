"""Proof that a to-do added over HTTP comes back, and is still there afterwards.

Decision 017: each test gets its own empty database. The session the routes use
is overridden to point at it, so a test run can never touch real to-dos.

Note the plain `TestClient(app)` — not `with TestClient(app)`. The context
manager form runs the app's lifespan, which would migrate whatever database the
app was imported against. The fixture runs the migration itself instead.
"""

import importlib

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text


@pytest.fixture
def client(tmp_path, monkeypatch):
    """A client whose routes read and write a fresh database, thrown away after."""
    db_path = tmp_path / "test.db"
    monkeypatch.setenv("TODO_DATABASE_URL", f"sqlite:///{db_path}")

    import app.db

    db = importlib.reload(app.db)
    db.run_migrations()

    from app.main import app as fastapi_app, get_session

    def session_for_this_test():
        with db.SessionLocal() as session:
            yield session

    fastapi_app.dependency_overrides[get_session] = session_for_this_test
    test_client = TestClient(fastapi_app)
    test_client.db_path = db_path
    yield test_client
    fastapi_app.dependency_overrides.clear()


def test_adding_a_todo_gives_back_the_whole_thing(client):
    response = client.post("/todos", json={"text": "buy milk"})

    assert response.status_code == 201

    body = response.json()
    assert body["text"] == "buy milk"
    assert body["done"] is False
    assert body["id"] > 0
    assert body["created_at"] is not None


def test_todos_come_back_in_the_order_they_were_added(client):
    for todo in ("buy milk", "walk dog", "file taxes"):
        client.post("/todos", json={"text": todo})

    listed = client.get("/todos").json()

    assert [t["text"] for t in listed] == ["buy milk", "walk dog", "file taxes"]


def test_the_list_starts_empty(client):
    assert client.get("/todos").json() == []


def test_a_todo_survives_a_restart(client):
    client.post("/todos", json={"text": "still here tomorrow"})

    # Nothing of the running app is reused: a new engine, opening the file the
    # way a second run of the program would.
    restarted = create_engine(f"sqlite:///{client.db_path}")
    with restarted.connect() as connection:
        rows = list(connection.execute(text("SELECT text FROM todos")))

    assert [row[0] for row in rows] == ["still here tomorrow"]


@pytest.mark.parametrize("bad_text", ["", "   ", "x" * 501])
def test_junk_text_is_refused_and_nothing_is_stored(client, bad_text):
    response = client.post("/todos", json={"text": bad_text})

    assert response.status_code == 422
    assert client.get("/todos").json() == []


def test_surrounding_whitespace_is_stripped(client):
    body = client.post("/todos", json={"text": "  buy milk  "}).json()

    assert body["text"] == "buy milk"
