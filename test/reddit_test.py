import pytest
import logging
logger = logging.getLogger(__name__)


from reddit.reddit_scraper import RedditScraper


@pytest.fixture
def reddit_scraper():
    scraper = RedditScraper()
    yield scraper

def test_query(reddit_scraper):
    posts = reddit_scraper.download_subreddit_data("wallstreetbets", 1)
    assert len(posts) == 1
    logger.info("downloaded post: " + posts[0].title)