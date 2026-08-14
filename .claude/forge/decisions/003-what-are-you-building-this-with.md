---
id: 003
question: What are you building this with?
status: decided
date: 2026-08-14
decided_by: user
affects: stack
content_sha: 42d7e26a4cd7e95c3ad54c41fae6fe1967d66fe151a6b636e45cbcb0c3050411
prev_sha: b4bd2c03852b86d67fc0ba328f6f63ce3ab2002621cbea3e21e2033fce0fa3e0
---

# C — Both together: a browser front end plus their own FastAPI back end and database

**Options considered**

- A — Front end only
- B — Back end only
- C — Both together
- D — Command line
- E — A phone app

**Recommended:** C — Both together · **Decided:** C — Both together: a browser front end plus their own FastAPI back end and database

## Why

The idea (decision 001) already named FastAPI and a simple front end, so C is what was described rather than a new choice. It is also the shape that teaches the thing they said they wanted to learn: how screens and an API talk to each other. B would leave them with no screen to look at; A would drop FastAPI, which is the point of the exercise. Single user, local only, so the extra parts cost nothing in hosting.

## In their words

Took the recommendation — it matches the FastAPI front-end-plus-back-end project they described as their first application for learning.
