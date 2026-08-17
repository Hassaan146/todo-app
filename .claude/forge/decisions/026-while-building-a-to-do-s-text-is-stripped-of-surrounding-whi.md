---
id: 026
question: While building: A to-do's text is stripped of surrounding whitespace and must be 1 to 500 characters, enforced by a pydantic StringConstraints annotation on the request model.
status: decided
date: 2026-08-15
decided_by: forge-builder
affects: phase-1.step-3
kind: build-note
content_sha: 4e29dd0a91fc211556cb1511e171af7d9cd772e8abbdc9b5a16c7abb53b0bef0
prev_sha: 7030c38d6b05b0c6b6cd66ad9439e68361b50a39ca9eb6dd33763c7b373b1709
---

# A to-do's text is stripped of surrounding whitespace and must be 1 to 500 characters, enforced by a pydantic StringConstraints annotation on the request model.

**Instead of:** Accepting any string the sender supplies, or writing a hand-rolled validator in the route.

## Why

Input crossing a trust boundary is validated before use, which is on the security floor and not something the local-only decision (006) waives — an unbounded body writes as much to disk as the sender feels like sending. Stripping first is what makes a whitespace-only to-do a 422 instead of an invisible row that cannot be deleted until phase 3. 500 is a cap chosen to be far above any real to-do; if it ever gets in the way it is one number in one place.
