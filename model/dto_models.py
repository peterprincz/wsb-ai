from dataclasses import dataclass
from typing import List, Optional

@dataclass
class SentinentDTO:
    stock_symbol: str
    rating:int
    
    def to_db(self):
        return SentinentDTO(stock_symbol=self.stock_symbol, rating = self.rating)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
@dataclass
class CommentDTO:
    id: str
    body: str
    score: int
    author: Optional[str]  # None if deleted or unavailable

@dataclass
class PostDTO:
    id: str
    title: str
    score: int
    url: str
    num_comments: int
    comments: List[CommentDTO]