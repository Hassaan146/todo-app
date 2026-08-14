"""The database: where it lives, what a to-do looks like, and how it is created.

Decision 021 kept this as one module rather than the usual db/models/migrations
split. There is one table; when there are two, this splits along the obvious
lines with no decisions in it.

Decision 016 chose SQLAlchemy, and decision 015 chose hand-written .sql
migrations — so the migration creates the table and the model only maps to it.
Nothing here calls `create_all()`.
"""

import os
from pathlib import Path

from sqlalchemy import Column, DateTime, Integer, String, create_engine, func, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MIGRATIONS_DIR = PROJECT_ROOT / "migrations"

# The database file, overridable so tests can point at their own (decision 017).
DATABASE_URL = os.environ.get("TODO_DATABASE_URL", f"sqlite:///{PROJECT_ROOT / 'todos.db'}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Todo(Base):
    """One to-do. The columns are decision 022; the table is migration 001."""

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    done = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, server_default=func.datetime("now"))


def run_migrations() -> list[str]:
    """Apply any .sql file in migrations/ that has not run yet, in name order.

    Which have run is recorded in the database itself, so it stays true even if
    the file is copied to another machine.
    """
    applied: list[str] = []

    with engine.begin() as connection:
        connection.execute(
            text(
                "CREATE TABLE IF NOT EXISTS schema_migrations ("
                "  name TEXT PRIMARY KEY,"
                "  applied_at TEXT NOT NULL DEFAULT (datetime('now'))"
                ")"
            )
        )
        already = {
            row[0] for row in connection.execute(text("SELECT name FROM schema_migrations"))
        }

        for path in sorted(MIGRATIONS_DIR.glob("*.sql")):
            if path.name in already:
                continue
            connection.execute(text(path.read_text(encoding="utf-8")))
            connection.execute(
                text("INSERT INTO schema_migrations (name) VALUES (:name)"),
                {"name": path.name},
            )
            applied.append(path.name)

    return applied
