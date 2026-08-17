---
id: 023
question: Is 'Add a to-do and list them back, through the interactive docs page, surviving a restart' worth building, and how much of it?
status: decided
date: 2026-08-14
decided_by: user
affects: lean:phase-1.step-3
content_sha: d5e15696a021cdddb1c269f57eb1230e25efac891627f78e5b1a7652940c9cfe
prev_sha: 22003155e707b833340fa2968606bc60c863f927035b15dc5b62082f16163171
---

# Two files touched: `app/main.py` gains two Pydantic models, a session dependency and `GET /todos` plus `POST /todos`; `tests/test_todos.py` is new.

**Instead of:** The conventional FastAPI split — a `schemas.py`, a `routers/todos.py` and wiring in main — for two endpoints, and the paging, sorting and filtering that phase 4 exists to decide.

**Before writing it, the ladder said**

- needed: Yes. This is what phase 1 promised and the only step that delivers it: without it the project has a table nothing can write to over HTTP.
- already: Half. app/db.py can already open a session and write a Todo, and tests/test_db.py proves a row survives being read back. What is missing is the HTTP end — nothing reaches that code from outside the process.
- stdlib: Most of it, and the framework is used rather than reimplemented. Pydantic validates the request body and returns FastAPI's 422 on bad input, so no validation layer is written; response models handle serialisation; /docs is generated from the type hints, which is what makes this step visible without a screen. SQLAlchemy binds every value, so no SQL is assembled by hand.
- smallest: Two Pydantic models (one in, one out), a session dependency, and two endpoint functions — about forty lines added to main.py — plus a test file. Nothing smaller still stores a to-do and lists it back.
- cost: A puts five things in main.py, and phase 3 adds three more endpoints, so this is the file that grows and the split will have to happen. The cost of doing it now is committing to a layout before phase 2's screen has shown whether the endpoint shape is right; the cost of deferring is one mechanical move later, with no decisions in it.

## Why

The third rung did the work here: almost everything this step could have hand-rolled — validation, error shapes for bad input, the documentation page, parameter binding — is already provided, so the honest size is two endpoint functions and the models around them. That left the real question as layout, and the case for splitting now is weaker than it looks: phase 2 is the first thing to exercise this API from outside, and it is the better moment to learn whether the shape is right. Option C was refused on the ladder rather than offered as merely larger: paging and sorting for a list with no rows in it is phase 4's decision taken early and without the information phase 4 will have.

## In their words

Took the recommendation — two endpoints do not need a router file yet, and it can be split when phase 3 makes main.py crowded.
