---
id: 017
question: What is in the database when you or a test opens it fresh?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: 14f8f15c65b3bc9d1c62b2a2419ae916b24c05fd3bb141dd073aff2907d5f6e8
prev_sha: 462b8c255a99e690cbd5e5650c4759cf274f0ffacdc6791d1f25c0def81ecdfa
---

# A — empty. Each test opens its own fresh database and creates whatever rows it needs. No seed file, and the real to-do database is never touched by a test run.

**Options considered**

- A — Empty, each test makes what it needs
- B — A seed file, committed
- C — A copy of real data, anonymised
- D — Whatever happens to be in there

**Recommended:** A — empty, per-test · **Decided:** A — empty. Each test opens its own fresh database and creates whatever rows it needs. No seed file, and the real to-do database is never touched by a test run.

## Why

Decision 010 makes passing tests part of finishing every step, so the trustworthiness of the suite is settled before the first test is written rather than after it starts lying. A test that passes only because an earlier test left a row behind is worse than no test, and per-test isolation removes that failure mode entirely for a few lines of fixture. A seed file was the real alternative and was rejected on cost: it rots silently unless something checks it, and the compensating pain — typing a to-do or two by hand when looking at the screen in phase 2 — is small and visible. The hard constraint recorded with it: tests point at their own database, never the file holding real to-dos, so a test run can never delete them.

## In their words

Took the recommendation — no test should pass because another test left something behind.
