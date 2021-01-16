import tweepy
import time
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def limit_handler(cursor):
    try:
        while True:
            try:
                yield cursor.next()
            except StopIteration:
                return
    except tweepy.RateLimitError:
        time.sleep(1000)


class TwitterClient:
    def __init__(self):
        consumer_key = os.getenv("KEY")
        consumer_secret = os.getenv("SECRET")
        BEARER = os.getenv("BEARER")
        ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
        ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(auth)

    def search_tweets(self):
        tweets = []
        for tweet in limit_handler(tweepy.Cursor(self.api.search, 'Starlink', lang='en', truncated=False).items(30)):
            try:
                # pprint(tweet)
                if tweet.retweet_count > 0:
                    if tweet not in tweets:
                        tweets.append(tweet)
                else:
                    tweets.append(tweet)
            except StopIteration:
                return tweets
            except tweepy.TweepError as e:
                print(e.reason)

        # tweets = self.api.search('Starlink', count=2, truncated=False)

        return tweets
