from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

class Sentinent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_symbol : str
    rating: int


# Create SQLite in-memory DB engine
engine = create_engine("sqlite:///:memory:")

# Create tables
SQLModel.metadata.create_all(engine)