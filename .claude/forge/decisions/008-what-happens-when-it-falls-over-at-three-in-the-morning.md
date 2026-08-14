---
id: 008
question: What happens when it falls over at three in the morning?
status: decided
date: 2026-08-14
decided_by: user
affects: failure
content_sha: 54a6e5cda722cba2158238636b0f4cd2a90d7f52cc1bf5f14e3bb71462e32a04
prev_sha: 2afb999612f90bbf607ab88980f88563576118fe95fbaa682cf2dfe9ece53b33
---

# B — readable logs. uvicorn's request log and full Python tracebacks printed to the terminal it runs in. No alerting, no log files, no restart supervision.

**Options considered**

- A — You find out when someone tells you
- B — It writes logs you can read afterwards
- C — It emails you when it breaks
- D — It restarts itself and tells you

**Recommended:** B — readable logs in the terminal · **Decided:** B — readable logs. uvicorn's request log and full Python tracebacks printed to the terminal it runs in. No alerting, no log files, no restart supervision.

## Why

The three-in-the-morning framing does not apply: decision 006 means nothing is running when they are not at the machine, so there is no outage window and nobody to notify. What survives is the useful half — when a request fails while they are using it, they should be able to see why. uvicorn gives that for free, and reading a traceback is the most transferable debugging skill in the project. Alerting (C) would need mail credentials to tell them something they are already watching happen; self-restart (D) would hide the failures they are trying to learn from.

## In their words

Took the recommendation — the logs are free and reading tracebacks is the part worth learning.
