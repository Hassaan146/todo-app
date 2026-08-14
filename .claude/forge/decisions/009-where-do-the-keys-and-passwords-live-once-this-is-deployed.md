---
id: 009
question: Where do the keys and passwords live once this is deployed?
status: decided
date: 2026-08-14
decided_by: user
affects: secrets
content_sha: 7620ccca6b539ede50cbddc7b6c7ae4c23277975e9547b684b2b0ca0da71b0e5
prev_sha: 54a6e5cda722cba2158238636b0f4cd2a90d7f52cc1bf5f14e3bb71462e32a04
---

# B — a `.env` file read as environment variables, listed in `.gitignore` from the first commit, with a committed `.env.example` carrying the variable names and no values.

**Options considered**

- A — Environment variables set by hand
- B — A .env file that is never committed
- C — Host's own secret store
- D — A dedicated secret manager

**Recommended:** B — a gitignored .env file · **Decided:** B — a `.env` file read as environment variables, listed in `.gitignore` from the first commit, with a committed `.env.example` carrying the variable names and no values.

## Why

The app has no secrets today: no sign-in (005), no external APIs, and a local SQLite file (004). The rule is set now anyway because the repository is public (cost fork) — a key committed once is in the history forever, and the moment to prevent that is before there is anything to commit. `.gitignore` and `.env.example` are written in the first step, not retrofitted. Environment variables set by hand (A) leak nothing but document nothing and are retyped every session; a host secret store (C) does not exist for this project because nothing hosts it (006); a secret manager (D) is team infrastructure.

## In their words

Took the recommendation — it is standard FastAPI practice and worth learning on a first project.
