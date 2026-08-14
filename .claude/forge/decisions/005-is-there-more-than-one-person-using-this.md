---
id: 005
question: Is there more than one person using this?
status: decided
date: 2026-08-14
decided_by: user
affects: people
content_sha: 7e504eb64bf48eb2a97f2fdf8e707aab68b1ec54c37a973e8b63ef0bb78357dd
prev_sha: 55a1e4eb08dba2936650758b33803852da2461599718aefdd8b660e7ca5c0c32
---

# A — Only me. No accounts, no sign-in, no per-user data separation.

**Options considered**

- A — Only me
- B — A few people I know
- C — Anyone who signs up
- D — Everyone in one organisation

**Recommended:** A — Only me · **Decided:** A — Only me. No accounts, no sign-in, no per-user data separation.

## Why

Decision 001 said this is for the author alone and is never deployed, so there is no second person to prove identity for and nothing to keep apart. Building accounts here would be weeks of work protecting a to-do list from nobody. The cost of the choice is honest and stated: because the app has no sign-in, it must stay bound to localhost — the moment it is reachable from another machine, anyone who can reach it can read and edit everything. That is a deployment decision, not something this record permits.

## In their words

Took the recommendation — it is for themselves only, so there is nobody to sign in.
