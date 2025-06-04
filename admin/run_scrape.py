from flask_admin import BaseView, expose
from flask import redirect, flash, url_for
import logging as log
from reddit.reddit_scraper import RedditScraper
from repository.reddit_repo import RedditRepository

class RunScape(BaseView):
    @expose('/')
    def index(self):
        log.info("Running webscrape")
        scraper = RedditScraper()
        postsDTO = scraper.download_subreddit_data("wallstreetbets", 2)
        for postDTO in postsDTO:
            RedditRepository.add(postDTO)
        flash("Function executed successfully!", "success")
        return redirect(url_for('admin.index')) 
