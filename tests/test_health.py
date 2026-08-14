"""Proof that the app starts and answers.

Decision 010: a step is not finished until its tests pass.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_answers_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
