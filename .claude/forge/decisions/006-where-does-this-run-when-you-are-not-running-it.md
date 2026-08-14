---
id: 006
question: Where does this run when you are not running it?
status: decided
date: 2026-08-14
decided_by: user
affects: delivery
content_sha: f0b5bbedae85e160cf2f657525f8f0729e14953b2528a7afd7e56bede427f95b
prev_sha: 7e504eb64bf48eb2a97f2fdf8e707aab68b1ec54c37a973e8b63ef0bb78357dd
---

# A — Only on their own machine. Run locally with uvicorn, bound to 127.0.0.1. No hosting, no containers, no deployment step.

**Options considered**

- A — Only on my machine
- B — A service that runs it for me
- C — A small server I rent
- D — An image anyone can run
- E — Files on a static host

**Recommended:** A — Only on my machine · **Decided:** A — Only on their own machine. Run locally with uvicorn, bound to 127.0.0.1. No hosting, no containers, no deployment step.

## Why

Stated plainly in decision 001: they do not want to deploy it anywhere. It follows from decision 005 as well — the app has no sign-in, so localhost is not merely the cheapest option but the only safe one. Binding to 127.0.0.1 rather than 0.0.0.0 is part of this decision, not an implementation detail: on 0.0.0.0 anyone on the same network could read and edit the to-dos. Hosting (B) would require building accounts first. Containers (D) would be a second thing to learn with no benefit while the app runs on one machine.

## In their words

Took the recommendation — they said from the start they don't want to deploy it anywhere; it is for personal learning.
