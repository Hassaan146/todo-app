-- Decision 022: a to-do is an id, its text, whether it is done, and when it was
-- made. `done` is unused until phase 3 and is here because a to-do that cannot
-- be completed is a different thing, not a smaller one.

CREATE TABLE todos (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    text       TEXT    NOT NULL,
    done       INTEGER NOT NULL DEFAULT 0,
    created_at TEXT    NOT NULL DEFAULT (datetime('now'))
);
