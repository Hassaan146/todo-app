---
id: 020
question: Is 'A FastAPI app that starts and answers on 127.0.0.1, with the database file and secrets excluded from git before either exists' worth building, and how much of it?
status: decided
date: 2026-08-14
decided_by: user
affects: lean:phase-1.step-1
content_sha: 4024119786bfd98f1561086a4d78b895841983cd8badd5c70dfd103dd5ab3f3a
prev_sha: 5ac98f48584fbf158364828165a3eb713c606ceda6e47bb0c97b65076d1ef332
---

# Five files: `.gitignore`, `requirements.txt`, `app/main.py` with a single GET /health route, `tests/test_health.py`, and a `README.md` carrying the activate-and-start commands.

**Instead of:** The full FastAPI layout — a settings module, a routers package, __init__ files and a .env.example — for an app with one route and no configuration.

**Before writing it, the ladder said**

- needed: Yes. Something has to start and answer before a table or an endpoint is worth writing, and the ignore rules have to exist before the database file does — the repository is public, and to-dos pushed to it cannot be taken back.
- already: No. The repository contains .claude/forge decision records and nothing else: no Python, no .gitignore, no dependency manifest.
- stdlib: Largely yes, and it is used rather than rebuilt. uvicorn binds 127.0.0.1, git does the ignoring with no code at all, and FastAPI's own /docs page proves the server is up without a status page being written. GitHub's Python .gitignore template is the starting point rather than a hand-written list.
- smallest: Four files: .gitignore, requirements.txt, app/main.py with one route, and a test for it. The user chose to add a fifth, README.md, with the two commands needed to start it.
- cost: Each extra file is one more thing to keep true. The README is the cheapest of them and the one most likely to rot, so it holds two commands and nothing that duplicates the decision records. .env.example was cut outright: with no variables to list it would be a file that lies, and the .gitignore entry already protects the day one appears.

## Why

The ladder removed the full-layout option before it reached the user: a settings module and a routers package are structure for an app that does not exist yet, and decision 016 already brings SQLAlchemy, so the only real question left was how many supporting files. It also cut .env.example, which decision 009 had implied — the ignore rule is what does the work, and an example file with nothing in it is worse than absent. The user went one step above the smallest version and took the README, which is a fair trade: five lines, and the alternative is re-deriving the start command from scrolled-away output.

## In their words

Chose B — wanted the start commands written down in a file rather than in output that scrolls away.
