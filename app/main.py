"""The FastAPI application.

Decision 006: this runs on 127.0.0.1 only. There is no sign-in (decision 005),
so anything that can reach this server can read and edit every to-do. Binding
to 127.0.0.1 rather than 0.0.0.0 is what keeps "anything" to this machine.
"""

from fastapi import FastAPI

app = FastAPI(
    title="todo-app",
    description="A personal to-do list. One user, one machine.",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Answer that the server is up.

    One route, so there is something to open in a browser and something for a
    test to assert on before any to-do exists.
    """
    return {"status": "ok"}
