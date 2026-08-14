"""The FastAPI application.

Decision 006: this runs on 127.0.0.1 only. There is no sign-in (decision 005),
so anything that can reach this server can read and edit every to-do. Binding
to 127.0.0.1 rather than 0.0.0.0 is what keeps "anything" to this machine.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import run_migrations


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Bring the database up to date before the first request is served."""
    applied = run_migrations()
    if applied:
        print(f"Applied migrations: {', '.join(applied)}")
    yield


app = FastAPI(
    title="todo-app",
    description="A personal to-do list. One user, one machine.",
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict[str, str]:
    """Answer that the server is up.

    One route, so there is something to open in a browser and something for a
    test to assert on before any to-do exists.
    """
    return {"status": "ok"}
