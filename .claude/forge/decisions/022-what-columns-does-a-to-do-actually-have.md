---
id: 022
question: What columns does a to-do actually have?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-2
content_sha: 22003155e707b833340fa2968606bc60c863f927035b15dc5b62082f16163171
prev_sha: 8c58366ac6e39b41631058c080967c631d6b8fd2cc0c99babdb4dfdf78b47f04
---

# B — `id`, `text`, `done`, `created_at`. The done flag exists from migration 001 but nothing in phase 1 reads or writes it; phase 3 turns it on without a schema change.

**Options considered**

- A — id, text, created_at
- B — id, text, done, created_at
- C — everything a to-do might want

**Recommended:** A — id, text, created_at (Forge recommended this; the user chose B, and the disagreement is recorded here) · **Decided:** B — `id`, `text`, `done`, `created_at`. The done flag exists from migration 001 but nothing in phase 1 reads or writes it; phase 3 turns it on without a schema change.

## Why

Forge recommended A and the user chose B; the disagreement is recorded rather than argued. Forge's case was that a column phase 1 never reads is a column nobody can test, and that phase 3 adding it would be the moment the hand-written migrations of decision 015 actually teach something. The user's case is that `done` is part of what a to-do is, not a phase 3 feature — which is fair: a to-do list where nothing can be completed is not a smaller version of the product, it is a different one. Cost accepted: the column ships unexercised for two phases, and the first real migration is now deferred to whenever phase 4 needs one. `created_at` is in regardless, because rows written without it can never truthfully be given one later. Everything beyond these four was rejected — due dates, priority and tags are features nobody has asked for, and SQLite makes dropping a column awkward enough that they would simply stay.

## In their words

Chose B over the recommendation — the done flag is part of what a to-do is, so it belongs in the table from the start.
