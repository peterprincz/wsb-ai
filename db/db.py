from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

# Create SQLite in-memory DB engine
engine = create_engine("sqlite:///:memory:")

# Create tables
SQLModel.metadata.create_all(engine)

