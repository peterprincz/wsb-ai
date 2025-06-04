from reddit.reddit_scraper import PostDTO
from repository.database import db
from model.dao_models import CommentDAO, PostDAO, SentinentDAO

class RedditRepository:
    
    @staticmethod
    def add(postDTO: PostDTO) -> None:
        db.session.add(PostDAO(id=postDTO.id, content=postDTO.title))
        for commentDTO in postDTO.comments:
            commentDao = CommentDAO(id=commentDTO.id, post_id=postDTO.id, content=commentDTO.body)
            db.session.add(commentDao)
        db.session.commit()

    @staticmethod
    def get_all() -> list[SentinentDAO]:
        return db.session.query(SentinentDAO).all()