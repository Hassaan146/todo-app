---
id: 011
question: Accept the four-phase plan?
status: decided
date: 2026-08-14
decided_by: user
affects: plan-accepted
content_sha: 6ca1d838ae6d490c89e17e659d5a5fbdfe15e557346c54d387ba085b0f2b3ef0
prev_sha: 3938a36e2ea6483b417b5139b2ac27430747ac76b2da1ca41bf10e2252648bdb
---

# Accepted — four phases, built in the order shown: the API, the screen, done/edit/delete, then filtering and ordering.

**Options considered**

- Accept all four phases in this order
- Drop phase 4 and stop at a working list
- Change the shape — add, split, merge or drop

**Recommended:** Accept the four phases · **Decided:** Accepted — four phases, built in the order shown: the API, the screen, done/edit/delete, then filtering and ordering.

## Why

Each phase delivers something usable on its own, so the project is never in a half-state they cannot look at. There is deliberately no testing phase: decision 010 makes passing tests part of finishing every step, so a phase for it would be work already done. The order puts the API first because the screen in phase 2 needs something to talk to, and defers polish to phase 4 where it can be dropped without losing a working app.

## In their words

Accepted the shape as presented, including phase 4.
