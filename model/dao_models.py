from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class SentinentDAO(SQLModel, table=True):
    __tablename__ = "sentinent" # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_id : Optional[str] = Field(default=None, foreign_key="stock.id")
    rating: int = Field(index=True)
    stock: Optional["StockDAO"] = Relationship(back_populates="sentinents")

class StockDAO(SQLModel, table=True):
    __tablename__ = "stock" # type: ignore
    id: Optional[str] = Field(default=None, primary_key=True)
    name: str
    sentinents: List[SentinentDAO] = Relationship(back_populates="stock")

class CommentDAO(SQLModel, table=True):
    __tablename__ = "comment" # type: ignore
    id: Optional[str] = Field(default=None, primary_key=True)
    post_id : Optional[str] = Field(default=None, foreign_key="post.id")
    content: str
    post: Optional["PostDAO"] = Relationship(back_populates="comments")

class PostDAO(SQLModel, table=True):
    __tablename__ = "post" # type: ignore
    id: Optional[str] = Field(default=None, primary_key=True)
    content: str
    comments: List[CommentDAO] = Relationship(back_populates="post")

SentinentDAO.model_rebuild()
StockDAO.model_rebuild()
CommentDAO.model_rebuild()
PostDAO.model_rebuild()