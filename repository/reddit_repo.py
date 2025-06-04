from reddit.reddit_scraper import PostDTO
from repository.database import db
from model.db_models import Comment, Post, Sentinent

class RedditRepository:
    @staticmethod

    def add(postDTO: PostDTO) -> None:
        comments = []
        for commentDTO in postDTO.comments:
            comments.append(Comment(post_id=commentDTO.id, content=commentDTO.body))
        db.session.add(Post(id=postDTO.id, content=postDTO.title, comments=comments))
        db.session.commit()

    @staticmethod
    def get_all() -> list[Sentinent]:
        return db.session.query(Sentinent).all()