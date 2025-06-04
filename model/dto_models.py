from dataclasses import dataclass

from model.db_models import Sentinent


@dataclass
class SentinentDTO:
    stock_symbol: str
    rating:int
    
    def to_db(self) -> Sentinent:
        return Sentinent(stock_symbol=self.stock_symbol, rating = self.rating)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)