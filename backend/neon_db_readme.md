# TaskFlow — Use Neon as the Single PostgreSQL Database

## Goal

From this point onward, TaskFlow will use **Neon PostgreSQL** as its single development database.

This means:

```text
Windows 11 ───┐
              │
Linux Mint ───┼── Internet ──> Neon PostgreSQL
              │
Deployed API ─┘
```

You no longer need to install or manage PostgreSQL locally on every operating system.

---

# 1. Why Use Neon?

Using Neon solves the main problem of switching between Windows and Linux.

Instead of managing:

```text
PostgreSQL installation
PostgreSQL service
ports like 5432 / 5433
database users
local database files
WSL networking
```

we use one hosted PostgreSQL database.

Your development flow becomes:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
Internet
   ↓
Neon PostgreSQL
```

Neon is still real PostgreSQL.

Only the location of the database changes.

---

# 2. Create a Neon Account

Go to:

```text
https://neon.com
```

Create a free account.

Then create a new project.

Suggested project name:

```text
TaskFlow
```

Neon will create a PostgreSQL database for you.

The database may be named something like:

```text
neondb
```

That is fine.

---

# 3. Get the Connection String

Inside your Neon project, open:

```text
Connect
```

or:

```text
Connection Details
```

Copy the PostgreSQL connection string.

It will look similar to:

```text
postgresql://username:password@hostname/neondb?sslmode=require
```

Your real value will be different.

Treat the connection string like a password.

Do not:

```text
commit it to GitHub
share it publicly
put it in screenshots
```

---

# 4. Update TaskFlow `.env`

Inside:

```text
taskflow/backend/
```

create or update:

```text
.env
```

Add:

```dotenv
DATABASE_URL=your_neon_connection_string_here
```

Example structure:

```dotenv
DATABASE_URL=postgresql://username:password@hostname/neondb?sslmode=require
```

Use the exact connection string Neon gives you.

---

# 5. Update `.gitignore`

Make sure:

```text
taskflow/backend/.gitignore
```

contains:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

Your real database connection string should never be committed.

---

# 6. Keep an `.env.example`

Create:

```text
.env.example
```

Add:

```dotenv
DATABASE_URL=your_postgresql_connection_string
```

This file can be committed to Git.

It tells another developer which environment variables are required without exposing secrets.

---

# 7. Install / Restore Python Dependencies

Your TaskFlow backend should use:

```text
FastAPI
SQLAlchemy
psycopg
python-dotenv
```

If these are already listed in:

```text
pyproject.toml
```

and you have:

```text
uv.lock
```

then on a new machine run:

```bash
uv sync
```

`uv` will create the correct `.venv` for the current operating system and install the dependencies.

Do not copy `.venv` between Windows and Linux.

If you copied TaskFlow from Windows to Linux Mint:

```bash
cd taskflow/backend
rm -rf .venv
uv sync
```

---

# 8. Update `database.py`

Replace the old local PostgreSQL configuration with a single `DATABASE_URL`.

Use:

```python
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


load_dotenv(Path(__file__).with_name(".env"))


DATABASE_URL = os.environ["DATABASE_URL"]


if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1,
    )

elif DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql+psycopg://",
        1,
    )


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


def get_db():
    with Session(engine) as db:
        yield db
```

---

# 9. Why `postgresql+psycopg://`?

Neon may provide:

```text
postgresql://...
```

But our project uses:

```text
psycopg
```

with SQLAlchemy.

So our code converts:

```text
postgresql://
```

into:

```text
postgresql+psycopg://
```

This tells SQLAlchemy to use the Psycopg driver.

---

# 10. `models.py` Does Not Change

Your SQLAlchemy model can remain the same.

Example:

```python
from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )
```

The model does not care whether PostgreSQL is local or hosted online.

---

# 11. `schemas.py` Does Not Change

Your Pydantic schemas also stay the same.

Example:

```python
from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=200,
    )

    description: str | None = None

    completed: bool = False


class TaskResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    title: str
    description: str | None
    completed: bool
```

---

# 12. Create the `tasks` Table in Neon

Open the Neon SQL Editor.

Run:

```sql
CREATE TABLE tasks (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT FALSE
);
```

Check:

```sql
SELECT * FROM tasks;
```

The result will initially be empty.

---

# 13. Start FastAPI

From:

```text
taskflow/backend/
```

run:

```bash
uv run fastapi dev main.py
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 14. Test `POST /tasks`

Use:

```json
{
    "title": "Connect TaskFlow to Neon",
    "description": "Use a hosted PostgreSQL database",
    "completed": false
}
```

Execute the request.

Then run:

```text
GET /tasks
```

You should see the new task.

---

# 15. Verify the Task in Neon

Return to the Neon SQL Editor.

Run:

```sql
SELECT * FROM tasks;
```

The task created through FastAPI should appear.

This confirms:

```text
Swagger
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
Neon PostgreSQL
```

---

# 16. Switching Between Windows and Linux Mint

The same Neon database can be used from both systems.

## On Windows

Clone or copy the project.

Then:

```bash
cd taskflow/backend
uv sync
```

Create:

```text
.env
```

with:

```dotenv
DATABASE_URL=your_neon_connection_string
```

Run:

```bash
uv run fastapi dev main.py
```

---

## On Linux Mint

Clone or copy the project.

Then:

```bash
cd taskflow/backend
rm -rf .venv
uv sync
```

Create:

```text
.env
```

with the same:

```dotenv
DATABASE_URL=your_neon_connection_string
```

Run:

```bash
uv run fastapi dev main.py
```

Both systems now use the same database.

---

# 17. Do Not Copy `.venv` Between Operating Systems

A Windows `.venv` contains Windows-specific files.

Linux expects different executables and paths.

So when moving TaskFlow from Windows to Linux:

```bash
rm -rf .venv
uv sync
```

This creates a fresh Linux virtual environment.

Likewise, on Windows, create a Windows environment with:

```bash
uv sync
```

---

# 18. Your New Daily Workflow

On either Windows or Linux:

```bash
cd taskflow/backend
```

Run:

```bash
uv run fastapi dev main.py
```

If dependencies changed:

```bash
uv sync
```

No local PostgreSQL service is required.

You no longer need commands like:

```text
sudo service postgresql start
pg_lsclusters
psql -h 127.0.0.1
```

for normal development.

---

# 19. New TaskFlow Architecture

```text
          Windows 11
              │
              ▼
          FastAPI
              │
              ▼
          SQLAlchemy
              │
              ▼
            psycopg
              │
              ▼
        Neon PostgreSQL
              ▲
              │
            psycopg
              ▲
              │
          SQLAlchemy
              ▲
              │
          FastAPI
              ▲
              │
          Linux Mint
```

Both development machines use the same hosted PostgreSQL database.

---

# 20. Important Security Rules

Never commit:

```text
.env
DATABASE_URL
database passwords
JWT secret keys
```

Commit:

```text
.env.example
```

but not:

```text
.env
```

---

# 21. Recommended Git Files

Your backend should contain:

```text
backend/
├── .env                 # private, NOT committed
├── .env.example         # safe to commit
├── .gitignore
├── database.py
├── main.py
├── models.py
├── schemas.py
├── pyproject.toml
└── uv.lock
```

---

# 22. Checklist

- [ ] Neon account created
- [ ] TaskFlow Neon project created
- [ ] Connection string copied
- [ ] `.env` contains `DATABASE_URL`
- [ ] `.env` is ignored by Git
- [ ] `.env.example` created
- [ ] `.venv` recreated for the current operating system
- [ ] `uv sync` completed
- [ ] `database.py` updated
- [ ] `tasks` table created in Neon
- [ ] FastAPI starts
- [ ] `POST /tasks` works
- [ ] `GET /tasks` works
- [ ] Task appears in Neon SQL Editor
- [ ] Windows and Linux can use the same Neon database

---

# Result

TaskFlow now uses:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
Neon PostgreSQL
```

This will be our PostgreSQL setup going forward.
