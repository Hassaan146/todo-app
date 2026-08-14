---
type: build-plan
step: phase-1.step-1
files: 5
written: 5
---


# The files this step touches, in the order they are written

Skeleton first: the shape of the thing before the detail that fills it in.
Each one is explained before the next is written.

[x] .gitignore · explained · The list of paths git must never record: the SQLite database file, any local secrets file, the virtual environment, and Python's cache output.
[x] requirements.txt · explained · The five packages this project installs, each pinned to one exact version: fastapi, uvicorn, SQLAlchemy, pytest and httpx.
[x] app/main.py · explained · The FastAPI application object, and one route — `GET /health` — that returns `{"status": "ok"}`.
[x] tests/test_health.py · explained · One test: it calls `GET /health` and asserts the status is 200 and the body is exactly `{"status": "ok"}`.
[x] README.md · explained · Three commands: create and install the virtual environment once, start the server, run the tests. Plus one line on why the host is 127.0.0.1.
