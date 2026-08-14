---
id: 021
question: Is 'The to-dos table, created in the SQLite file when the app starts' worth building, and how much of it?
status: decided
date: 2026-08-14
decided_by: user
affects: lean:phase-1.step-2
content_sha: 8c58366ac6e39b41631058c080967c631d6b8fd2cc0c99babdb4dfdf78b47f04
prev_sha: 4024119786bfd98f1561086a4d78b895841983cd8badd5c70dfd103dd5ab3f3a
---

# Three files: `app/db.py` holding the engine, the session factory, the `Todo` model and the migration runner; `migrations/001_create_todos.sql`; and `tests/test_db.py`.

**Instead of:** The conventional five-file split — separate `db.py`, `models.py` and `migrations.py` modules — for a project with exactly one table.

**Before writing it, the ladder said**

- needed: Yes. Nothing in the project stores anything: step 1 built a server with one route and no persistence, and step 3 has nowhere to put a to-do until this exists.
- already: No. SQLAlchemy is pinned in requirements.txt and installed, but not imported by a single line of the project yet.
- stdlib: Partly, and the overlap is the interesting part. SQLAlchemy's metadata.create_all() would build the table from the model with no SQL written at all — but decision 015 chose numbered .sql files, so the migration creates the table and the model maps to it. That split is deliberate and was offered to the user as option C, which would have superseded 015 rather than quietly sitting beside it.
- smallest: Three files. One module can hold an engine, a session factory, one model and a fifteen-line migration runner and still fit on a screen; the .sql file and the test cannot be folded into anything.
- cost: A is one file with four responsibilities, which is the honest cost and the reason B exists. It stays legible while there is one table; the moment phase 3 or a second table makes it crowded, splitting it is a mechanical move with no decisions in it. B's cost is paid now and every time somebody follows three imports to answer one question.

## Why

The ladder's real finding was the third rung: SQLAlchemy can create tables itself, so the migration file is not technically required, and that made C a genuine option rather than a strawman — it was offered with its full cost, that it would replace decision 015. The user kept 015 and took the smallest layout. The remaining trade is file count against separation, and with one table the separation buys nothing that cannot be bought later for the same price.

## In their words

Took the recommendation — one table does not need three modules, and it can be split later if it gets crowded.
