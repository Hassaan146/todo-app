---
id: 018
question: What shape is the interface between the screens and the server?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: d14f670ced9d6a3db85e6f84bd844cfaedfdd9f3080bb7dc9f19cbc6970a6e02
prev_sha: 14f8f15c65b3bc9d1c62b2a2419ae916b24c05fd3bb141dd073aff2907d5f6e8
---

# A — REST. `GET /todos` and `POST /todos` for the collection, `/todos/{id}` for one item (PATCH and DELETE arrive in phase 3). JSON in, JSON out.

**Options considered**

- A — REST, one address per thing
- B — One endpoint per action
- C — GraphQL
- D — Server-rendered pages, no API

**Recommended:** A — REST · **Decided:** A — REST. `GET /todos` and `POST /todos` for the collection, `/todos/{id}` for one item (PATCH and DELETE arrive in phase 3). JSON in, JSON out.

## Why

FastAPI is shaped for REST: the automatic docs page at /docs renders it without any work, which is exactly what makes phase 1 usable before there is a screen. Four addresses cover the whole project through phase 4. Endpoint-per-action was rejected because the endpoint list grows with every screen and never shrinks; GraphQL because a schema language and a library are a large cost for one table; server-rendered HTML because it would collapse phase 2 and remove the thing they said they wanted to learn — how a front end talks to an API. The known cost is REST's chattiness, which does not bite at this size. This contract is load-bearing: phases 2, 3 and 4 are all written against it.

## In their words

Took the recommendation — it is what FastAPI is built for and what the tutorials assume.
