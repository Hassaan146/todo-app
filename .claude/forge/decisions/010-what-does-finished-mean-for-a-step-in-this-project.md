---
id: 010
question: What does 'finished' mean for a step in this project?
status: decided
date: 2026-08-14
decided_by: user
affects: done
content_sha: 3938a36e2ea6483b417b5139b2ac27430747ac76b2da1ca41bf10e2252648bdb
prev_sha: 7620ccca6b539ede50cbddc7b6c7ae4c23277975e9547b684b2b0ca0da71b0e5
---

# C — the floor (tests pass, review clean), plus they have run it themselves, plus they can explain back what the step did before the next one starts.

**Options considered**

- A — The floor only
- B — The floor, and they have run it
- C — The floor, and they can explain it back
- Ruled out: someone else has looked — only one person uses this

**Recommended:** C — the teaching bar · **Decided:** C — the floor (tests pass, review clean), plus they have run it themselves, plus they can explain back what the step did before the next one starts.

## Why

Decision 001 said the point of this project is learning, not shipping. Under bar A they would end with a working to-do app and no idea how it works, which fails the actual goal while passing every automated check. C is the slowest bar and the only one aligned with why the project exists. The cost is real and accepted: every step ends with Forge asking them to explain it, and a step does not close until they can.

## In their words

Took the recommendation — the project is for learning, so code they cannot explain would not count as finished.
