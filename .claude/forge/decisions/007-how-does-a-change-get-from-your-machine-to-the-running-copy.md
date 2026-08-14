---
id: 007
question: How does a change get from your machine to the running copy?
status: decided
date: 2026-08-14
decided_by: user
affects: release
content_sha: 2afb999612f90bbf607ab88980f88563576118fe95fbaa682cf2dfe9ece53b33
prev_sha: f0b5bbedae85e160cf2f657525f8f0729e14953b2528a7afd7e56bede427f95b
---

# Not applicable — asked, and found irrelevant. There is no running copy to reach: decision 006 put the only copy on the author's own machine, so a change is live the moment the file is saved.

**Options considered**

- A — By hand
- B — On every push
- C — On push once tests pass
- D — A button once tests pass
- Not applicable — nothing is deployed

## Why

Every option here (by hand, on push, on green tests, on a button) describes a path from a development machine to a separate running copy. Decision 006 removed the far end of that path. Git push still happens on every step, but it publishes the history to GitHub — it does not release anything to anyone. If this project ever gains a hosted copy, decision 006 changes first and this question is asked again against that new answer.

## In their words

Follows from their own answers: they said they don't want to deploy it anywhere, so there is nowhere for a release to go.
