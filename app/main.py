"""The FastAPI application.

Decision 006: this runs on 127.0.0.1 only. There is no sign-in (decision 005),
so anything that can reach this server can read and edit every to-do. Binding
to 127.0.0.1 rather than 0.0.0.0 is what keeps "anything" to this machine.
"""

from contextlib import asynccontextmanager
from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict, StringConstraints
from sqlalchemy.orm import Session

from app.db import SessionLocal, Todo, run_migrations


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


def get_session():
    """Hand a route its own database session, and close it when the route ends."""
    with SessionLocal() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

# What a to-do's text is allowed to be. Stripped first, so "   " is empty and
# refused rather than stored as a row you cannot see. The 500 is a limit, not a
# rule about to-dos: without one, a request body is as large as the sender likes.
TodoText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=500)]


class TodoIn(BaseModel):
    """What you are allowed to send. Anything else gets FastAPI's 422."""

    text: TodoText


class TodoOut(BaseModel):
    """What comes back: the whole to-do, including the parts SQLite assigned.

    Decision 024 — `id` and `created_at` cannot be known by the caller, so the
    finished object is returned rather than making them ask a second time.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    text: str
    done: bool
    created_at: datetime


@app.get("/health")
def health() -> dict[str, str]:
    """Answer that the server is up.

    One route, so there is something to open in a browser and something for a
    test to assert on before any to-do exists.
    """
    return {"status": "ok"}


@app.post("/todos", response_model=TodoOut, status_code=201)
def add_todo(todo: TodoIn, session: SessionDep) -> Todo:
    """Store one to-do and give it back with its id and timestamp filled in."""
    stored = Todo(text=todo.text)
    session.add(stored)
    session.commit()
    session.refresh(stored)  # id and created_at are the database's to assign.
    return stored


@app.get("/todos", response_model=list[TodoOut])
def list_todos(session: SessionDep) -> list[Todo]:
    """Every to-do, oldest first. Sorting and paging are phase 4's decision."""
    return session.query(Todo).order_by(Todo.id).all()
