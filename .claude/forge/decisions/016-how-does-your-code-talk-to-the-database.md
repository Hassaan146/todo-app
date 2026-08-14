---
id: 016
question: How does your code talk to the database?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: 462b8c255a99e690cbd5e5650c4759cf274f0ffacdc6791d1f25c0def81ecdfa
prev_sha: 02e433c5e286549ee915fa2e09aaf2adca0bd92b660e7d6744fde945dc674a20
---

# C — SQLAlchemy. The ORM maps the to-dos table to a Python class and every query goes through a session.

**Options considered**

- A — Plain SQL in one module (sqlite3)
- B — SQLModel
- C — SQLAlchemy
- D — A query builder

**Recommended:** A — plain SQL in one module (Forge recommended this; the user chose C, and the disagreement is recorded here) · **Decided:** C — SQLAlchemy. The ORM maps the to-dos table to a Python class and every query goes through a session.

## Why

Forge recommended plain sqlite3 and the user chose SQLAlchemy; the disagreement is recorded rather than argued. Forge's case was that one table and roughly six queries do not need an ORM, and that an ORM's whole purpose is to hide the SQL a first project is trying to learn. The user's case is the stronger one over a longer horizon: SQLAlchemy is what they will meet in real Python work, and learning it on a project small enough to hold in their head is cheaper than learning it on a large one. Consequences accepted: one dependency added to requirements.txt, session lifecycle to understand, and generated SQL that is not visible unless they turn on echo. Two things this does not change — decision 015 still stands, so schema changes are the numbered .sql files and not Alembic, and the security floor still applies: values from the browser are bound parameters, which SQLAlchemy does by default and which raw text() would not.

## In their words

Chose SQLAlchemy over the recommendation — it is the ORM used in real Python projects and worth learning properly.
