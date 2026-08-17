---
id: 024
question: What comes back when you add a to-do?
status: decided
date: 2026-08-15
decided_by: user
affects: phase-1.step-3
content_sha: 0270343e705048c4f76dd3e7907a5281af3bd56d7447b92390118a57411a7a52
prev_sha: d5e15696a021cdddb1c269f57eb1230e25efac891627f78e5b1a7652940c9cfe
---

# A — `201 Created` with the whole new to-do as JSON: id, text, done, created_at.

**Options considered**

- A — 201 and the new to-do
- B — 201 and just the id
- C — 201 and the whole list
- D — 204 and nothing

**Recommended:** A — 201 and the new to-do · **Decided:** A — `201 Created` with the whole new to-do as JSON: id, text, done, created_at.

## Why

The id and created_at are assigned by the database, so the caller cannot know them and would have to ask a second time under every other option. Returning the finished object makes phase 2's screen straightforward: send the text, draw what comes back. It is also the ordinary REST answer, which matters given decision 018. Returning the whole list was rejected because it re-sends every to-do on every add and quietly couples writing to reading; 204 was rejected because it forces a refetch after each add. The known cost is accepted: if phase 2's screen turns out to refetch anyway, the body is written and never read.

## In their words

Took the recommendation — the screen gets what it needs in one request.
