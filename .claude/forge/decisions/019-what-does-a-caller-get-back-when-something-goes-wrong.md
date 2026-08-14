---
id: 019
question: What does a caller get back when something goes wrong?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: 5ac98f48584fbf158364828165a3eb713c606ceda6e47bb0c97b65076d1ef332
prev_sha: d14f670ced9d6a3db85e6f84bd844cfaedfdd9f3080bb7dc9f19cbc6970a6e02
---

# A — an HTTP status code and a plain message meant for a person, as `{"detail": "..."}`. Unexpected failures return a bare 500 with no internals; the traceback goes to the terminal only.

**Options considered**

- A — Status code and a human message
- B — Status code, machine-readable code, and a message
- C — Whatever FastAPI produces by default

**Recommended:** A — status code and a human message · **Decided:** A — an HTTP status code and a plain message meant for a person, as `{"detail": "..."}`. Unexpected failures return a bare 500 with no internals; the traceback goes to the terminal only.

## Why

There is one user and one screen (005), so nothing needs to branch on a stable machine-readable code — a message is what would be displayed regardless, and option B's extra convention would be maintained for a consumer that does not exist. Pydantic already returns well-shaped 422s for bad input at no cost, so this contract only covers the few errors raised deliberately, such as an id that is not there. FastAPI's raw defaults were rejected because unhandled exceptions are exactly where internals leak. The floor part is not a preference and is recorded as such: no stack trace, query or file path ever appears in a response, which pairs with decision 008 putting the traceback in the terminal where they can read it.

## In their words

Took the recommendation — one screen and one user, so a readable message is all that would ever be shown.
