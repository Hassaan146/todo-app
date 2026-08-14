---
type: build-plan
step: phase-1.step-2
files: 4
written: 4
---


# The files this step touches, in the order they are written

Skeleton first: the shape of the thing before the detail that fills it in.
Each one is explained before the next is written.

[x] migrations/001_create_todos.sql · explained · The first migration: the `CREATE TABLE todos` statement with the four columns decision 022 settled — id, text, done, created_at.
[x] app/db.py · explained · The engine pointing at the SQLite file, a session factory, the `Todo` model mapping to the todos table, and `run_migrations()` which applies any unrun `.sql` file in order.
[x] tests/test_db.py · explained · Four tests over a temporary database: the migration creates the todos table, its columns are exactly the four decision 022 named, a to-do written survives being read back, and running the migrations a second time does nothing.
[x] app/main.py · explained · A `lifespan` handler that calls `run_migrations()` once before the server accepts its first request, and prints the names of any that ran.
