from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Sentinent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_id : Optional[str] = Field(default=None, foreign_key="stock.id")
    rating: int = Field(index=True)
    stock: Optional["Stock"] = Relationship(back_populates="sentinents")

class Stock(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    name: str
    sentinents: List[Sentinent] = Relationship(back_populates="stock")

class Comment(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    post_id : Optional[str] = Field(default=None, foreign_key="post.id")
    content: str
    post: Optional["Post"] = Relationship(back_populates="comments")

class Post(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    content: str
    comments: List[Comment] = Relationship(back_populates="post")

Sentinent.model_rebuild()
Stock.model_rebuild()
Comment.model_rebuild()
Post.model_rebuild()