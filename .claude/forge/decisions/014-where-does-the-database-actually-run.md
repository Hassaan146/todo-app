---
id: 014
question: Where does the database actually run?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: abcc1fbce66d672cef90bde4ac32bcc18af56d6876288bb684f104243614f89f
prev_sha: ddc049d75cf669f8b6b4b99e8e5746e350a85dcc3818fad752dd412c1d5d899d
---

# On this machine, next to the code — a single SQLite file in the project folder, gitignored. Not re-asked; it follows from decisions 004 and 006.

**Options considered**

- On this machine, next to the code
- In a container beside the app
- A managed service you rent
- A server you already have

**Recommended:** On this machine, next to the code (carried from 004 and 006) · **Decided:** On this machine, next to the code — a single SQLite file in the project folder, gitignored. Not re-asked; it follows from decisions 004 and 006.

## Why

SQLite has no server to run anywhere: the database is a file the app opens, so "where it runs" is wherever the app runs, and decision 006 put that on the author's own machine only. A container (needs containers, ruled out in 006's reasoning as a second thing to learn) and a managed service (needs hosting, which 006 ruled out) are not available to this project. The consequence is stated rather than discovered: the file lives only on this machine and is excluded from git, so it is not backed up anywhere. Losing the machine loses the to-dos, which decision 004 already accepted as the cost.

## In their words

Follows from their own answers — SQLite (004) is a file, and they said it runs only on their machine (006).
