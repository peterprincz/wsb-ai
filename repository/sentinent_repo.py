from repository.database import db
from model.dao_models import SentinentDAO

class SentinentRepository:
    @staticmethod
    def add(sentinent: SentinentDAO) -> None:
        db.session.add(sentinent)
        db.session.commit()

    @staticmethod
    def get_all() -> list[SentinentDAO]:
        return db.session.query(SentinentDAO).all()

    @staticmethod
    def delete(sentinent: SentinentDAO) -> None:
        db.session.delete(sentinent)
        db.session.commit()

    @staticmethod
    def update() -> None:
        # Call commit after changing any objects tracked by session
        db.session.commit()