from repository.database import db
from model.db_models import Sentinent

class SentinentRepository:
    @staticmethod
    def add(sentinent: Sentinent) -> None:
        db.session.add(sentinent)
        db.session.commit()

    @staticmethod
    def get_all() -> list[Sentinent]:
        return db.session.query(Sentinent).all()

    @staticmethod
    def delete(sentinent: Sentinent) -> None:
        db.session.delete(sentinent)
        db.session.commit()

    @staticmethod
    def update() -> None:
        # Call commit after changing any objects tracked by session
        db.session.commit()