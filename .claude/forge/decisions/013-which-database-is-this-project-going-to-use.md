---
id: 013
question: Which database is this project going to use?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: ddc049d75cf669f8b6b4b99e8e5746e350a85dcc3818fad752dd412c1d5d899d
prev_sha: 6f07f1478e6490327f5e39e1ab3601e7fa74ba8fc373d17c7c002967b601442f
---

# SQLite, one file — already chosen in decision 004. Not re-asked.

**Options considered**

- SQLite, one file
- Postgres you run yourself
- MySQL or MariaDB
- MongoDB
- Supabase
- Neon

**Recommended:** SQLite, one file (carried from decision 004) · **Decided:** SQLite, one file — already chosen in decision 004. Not re-asked.

## Why

This is the engine's per-project database question, and the user answered it in the foundation as decision 004: SQLite in a single file, on the grounds that there is one user (005), it runs locally (006), and it is a real relational database with nothing to install. Putting the same choice on screen a second time would teach them that Forge does not read its own record. This record exists so the topic is tied to the build steps that need it; the reasoning and the user's own words live in 004, which it points at. The other options remain what they were: Postgres, MySQL and MongoDB all require running a server this project has no use for, and Supabase and Neon require hosting that decision 006 ruled out.

## In their words

Answered in decision 004: nothing to install or run, and they still learn how a real database works.
