"""Proof that the migration runs and the table is really there.

Decision 017: each test gets its own empty database. `TODO_DATABASE_URL` points
app.db somewhere temporary, so a test run can never touch real to-dos.
"""

import importlib

import pytest
from sqlalchemy import inspect, text


@pytest.fixture
def db(tmp_path, monkeypatch):
    """A freshly migrated, empty database, thrown away after the test."""
    monkeypatch.setenv("TODO_DATABASE_URL", f"sqlite:///{tmp_path / 'test.db'}")

    import app.db

    module = importlib.reload(app.db)
    module.run_migrations()
    return module


def test_migration_creates_the_todos_table(db):
    assert "todos" in inspect(db.engine).get_table_names()


def test_columns_are_what_decision_022_said(db):
    columns = {c["name"] for c in inspect(db.engine).get_columns("todos")}

    assert columns == {"id", "text", "done", "created_at"}


def test_a_todo_survives_being_written_and_read_back(db):
    with db.SessionLocal() as session:
        session.add(db.Todo(text="buy milk"))
        session.commit()

    with db.SessionLocal() as session:
        stored = session.query(db.Todo).one()

        assert stored.text == "buy milk"
        assert stored.done == 0
        assert stored.created_at is not None


def test_migrations_do_not_run_twice(db):
    assert db.run_migrations() == []

    with db.engine.connect() as connection:
        names = [row[0] for row in connection.execute(text("SELECT name FROM schema_migrations"))]

    assert names == ["001_create_todos.sql"]
