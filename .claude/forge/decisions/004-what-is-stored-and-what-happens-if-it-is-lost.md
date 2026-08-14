---
id: 004
question: What is stored, and what happens if it is lost?
status: decided
date: 2026-08-14
decided_by: user
affects: data
content_sha: 55a1e4eb08dba2936650758b33803852da2461599718aefdd8b660e7ca5c0c32
prev_sha: 42d7e26a4cd7e95c3ad54c41fae6fe1967d66fe151a6b636e45cbcb0c3050411
---

# A — SQLite, a single file on disk. Stored: to-do items (text, done/not done, timestamps). Losing the file loses the to-dos and nothing else.

**Options considered**

- A — SQLite, one file
- B — Postgres
- C — MySQL
- D — A hosted database
- E — Plain files (JSON/CSV)

**Recommended:** A — SQLite, one file · **Decided:** A — SQLite, a single file on disk. Stored: to-do items (text, done/not done, timestamps). Losing the file loses the to-dos and nothing else.

## Why

One user, running locally (decisions 001 and 003), so SQLite's only real limitation — several writers at once — cannot occur. It is a real relational database, so the tables, queries and migrations they learn transfer directly to Postgres later. Postgres or MySQL would mean installing and running a server before the first to-do could be added, which is cost with no lesson attached at this size. JSON files would avoid the install but teach nothing about databases. The data itself is low-stakes: personal to-dos that can be retyped, so the database file being untracked by git and unbacked-up is an accepted cost rather than an oversight.

## In their words

Took the recommendation — nothing to install or run, and they still learn how a real database works.
