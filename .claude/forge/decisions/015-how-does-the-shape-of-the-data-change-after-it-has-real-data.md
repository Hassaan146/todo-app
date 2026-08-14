---
id: 015
question: How does the shape of the data change after it has real data in it?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: 02e433c5e286549ee915fa2e09aaf2adca0bd92b660e7d6744fde945dc674a20
prev_sha: abcc1fbce66d672cef90bde4ac32bcc18af56d6876288bb684f104243614f89f
---

# A — numbered `.sql` migration files kept in `migrations/`, applied in order at startup, with a table recording which have already run.

**Options considered**

- A — Numbered .sql files run in order
- B — A migration tool (Alembic)
- C — The framework infers it from the models
- D — Delete the file and start again

**Recommended:** A — numbered .sql files · **Decided:** A — numbered `.sql` migration files kept in `migrations/`, applied in order at startup, with a table recording which have already run.

## Why

The project is one table with about two shape changes ahead of it (the done flag in phase 3, possibly an ordering column in phase 4). The loader is roughly fifteen lines and adds no dependency, and writing the SQL by hand is the part that actually teaches what a migration is — which is the point under decision 010's bar. Alembic is the correct answer on a larger project and would be a whole tool's vocabulary learned before the first to-do exists. Framework inference was rejected because SQLite's limited ALTER TABLE support is exactly where inferred migrations go wrong quietly. Rebuilding from nothing was rejected outright: it would delete their real to-dos on every shape change.

## In their words

Took the recommendation — small, no dependency, and it teaches what a migration actually is.
