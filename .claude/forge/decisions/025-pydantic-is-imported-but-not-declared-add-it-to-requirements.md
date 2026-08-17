---
id: 025
question: Pydantic is imported but not declared. Add it to requirements.txt?
status: decided
date: 2026-08-15
decided_by: user
affects: phase-1.step-3
content_sha: 7030c38d6b05b0c6b6cd66ad9439e68361b50a39ca9eb6dd33763c7b373b1709
prev_sha: 0270343e705048c4f76dd3e7907a5281af3bd56d7447b92390118a57411a7a52
---

# Add pydantic to requirements.txt as a declared dependency

**Options considered**

- Add pydantic to requirements.txt explicitly
- Leave it undeclared and rely on FastAPI pulling it in transitively
- Stop importing pydantic and hand-validate request bodies

**Recommended:** Add pydantic to requirements.txt explicitly · **Decided:** Add pydantic to requirements.txt as a declared dependency

## Why

The app imports pydantic for request/response models, so it is a real runtime dependency. Declaring it in requirements.txt means a fresh venv installs it explicitly rather than relying on it arriving as a FastAPI transitive dependency, which could change version or disappear on a FastAPI upgrade.

## In their words

yes add pydantic for input verification
