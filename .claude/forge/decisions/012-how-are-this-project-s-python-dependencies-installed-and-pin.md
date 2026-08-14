---
id: 012
question: How are this project's Python dependencies installed and pinned?
status: decided
date: 2026-08-14
decided_by: user
affects: phase-1.step-1
content_sha: 6f07f1478e6490327f5e39e1ab3601e7fa74ba8fc373d17c7c002967b601442f
prev_sha: 6ca1d838ae6d490c89e17e659d5a5fbdfe15e557346c54d387ba085b0f2b3ef0
---

# A — a `venv` virtual environment in `.venv/`, with dependencies pinned in `requirements.txt`. `.venv/` is gitignored; `requirements.txt` is committed.

**Options considered**

- A — venv + requirements.txt
- B — uv
- C — Poetry
- D — Install globally, no environment

**Recommended:** A — venv + requirements.txt · **Decided:** A — a `venv` virtual environment in `.venv/`, with dependencies pinned in `requirements.txt`. `.venv/` is gitignored; `requirements.txt` is committed.

## Why

venv ships with Python, so there is nothing to install before the project starts, and it is what every FastAPI tutorial they read next will assume — which matters on a learning project (001, 010). uv is faster but adds a tool and a vocabulary before the first to-do; Poetry adds packaging concepts this project will never use, since nothing is published (006). Global install was rejected outright: it changes the machine rather than the folder, and every later Python project would inherit these packages. Pinned versions in requirements.txt are what make the project rebuildable from the public repo.

## In their words

Took the recommendation — nothing extra to install, and it matches the tutorials they will be reading.
