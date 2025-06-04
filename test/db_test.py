import pytest
from sqlmodel import SQLModel, create_engine, Session, select
from model.db_models import Sentinent

@pytest.fixture
def session():
    # Create an in-memory SQLite engine
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)  # Create tables fresh for each test

    with Session(engine) as session:
        yield session
        # Session closes automatically with context manager

def test_add_sentinent(session):
    sentinent = Sentinent(stock_symbol="AMD", rating=3)
    session.add(sentinent)
    session.commit()

    statement = select(Sentinent).where(Sentinent.stock_symbol == "AMD")
    result = session.exec(statement)
    queried = result.one()
    
    assert queried.rating == 3

def test_empty_db(session):
    statement = select(Sentinent)
    result = session.exec(statement)
    sentinents = result.all()
    assert sentinents == []