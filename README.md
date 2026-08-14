# todo-app

A personal to-do list. One user, one machine, not deployed anywhere.

Built with [Forge Mentor](https://github.com/Hassaan146/todo-app/tree/main/.claude/forge) —
every decision behind this code is recorded in `.claude/forge/decisions/`.

## Setup, once

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run it

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Then open <http://127.0.0.1:8010/docs>.

Port 8010 rather than 8000 because something else on this machine already
listens on 8000. Any free port works; keep the README and what you run in step.

`--host 127.0.0.1` is deliberate. There is no sign-in, so anything that can
reach this server can read and change every to-do. Keep it off `0.0.0.0`.

## Test it

```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest
```
