from dataclasses import dataclass, field
from typing import List, Optional
import praw
from config.appconfig import config


@dataclass
class Comment:
    id: str
    body: str
    score: int
    author: Optional[str]  # None if deleted or unavailable

@dataclass
class Post:
    id: str
    title: str
    score: int
    url: str
    num_comments: int
    comments: List[Comment] = field(default_factory=list)

class RedditScraper:

    def __init__(self) -> None:
        self.reddit = praw.Reddit(
            client_id = config.client_id,
            client_secret = config.client_secret,
            password = config.password,
            user_agent = config.user_agent,
            username = config.username,
        )

    def download_subreddit_data(self, subreddit_name: str, limit: int = 10) -> List[Post]:
        subreddit = self.reddit.subreddit(subreddit_name)
        posts: List[Post] = []

        for submission in subreddit.top(limit=limit):
            submission.comments.replace_more(limit=0)
            comments: List[Comment] = [
                Comment(
                    id=comment.id,
                    body=comment.body,
                    score=comment.score,
                    author=str(comment.author) if comment.author else None,
                )
                for comment in submission.comments.list()
            ]

            post = Post(
                id=submission.id,
                title=submission.title,
                score=submission.score,
                url=submission.url,
                num_comments=submission.num_comments,
                comments=comments,
            )
            posts.append(post)

        return posts