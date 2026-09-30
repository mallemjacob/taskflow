import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session


load_dotenv(Path(__file__).with_name(".env"))

DATABASE_URL = URL.create(
    "postgresql+psycopg",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    database=os.environ["DB_NAME"]
)

engine = create_engine(DATABASE_URL)


def get_db():
    with Session(engine) as db:
        yield db
