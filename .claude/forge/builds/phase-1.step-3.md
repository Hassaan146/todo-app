---
type: build-plan
step: phase-1.step-3
files: 3
written: 3
---


# The files this step touches, in the order they are written

Skeleton first: the shape of the thing before the detail that fills it in.
Each one is explained before the next is written.

[x] requirements.txt · explained · One added line, pydantic==2.13.4, declaring the validation library the app imports directly.
[x] app/main.py · explained · Two routes — POST /todos and GET /todos — with a session dependency and the two Pydantic models around them.
[x] tests/test_todos.py · explained · Seven tests over the two new routes: the 201 body, list order, the empty list, survival of a restart, three kinds of refused text, and whitespace stripping.
