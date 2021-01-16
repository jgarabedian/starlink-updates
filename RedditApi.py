from praw import Reddit
import os
from dotenv import load_dotenv

load_dotenv()

secret = os.getenv("REDDIT_SECRET")
client = os.getenv("REDDIT_CLIENT")
user = os.getenv("REDDIT_USERNAME")
pwd = os.getenv("REDDIT_PWD")

class RedditClient:
    def __init__(self):
        self.api = Reddit(
            client_id=client,
            client_secret=secret,
            user_agent="*",
            redirect_uri="http://127.0.0.1:5000/"
        )
        # url = self.api.auth.url(["identity", "read"], "ilkjli", "permanent")

    def get_hot_posts(self):
        posts = self.api.subreddit('Starlink').hot(limit=20)
        return posts


if __name__ == "__main__":
    reddit = RedditClient()
    posts = reddit.get_hot_posts()
    for post in posts:
        import pprint
        # pprint.pprint(vars(post))
        print(post.url)