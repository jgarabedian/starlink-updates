from flask import Flask, render_template, flash, request, redirect, Response, abort, url_for
from flaskext.markdown import Markdown
from datetime import datetime
from TwitterApi import TwitterClient
from RedditApi import RedditClient


app = Flask(__name__)
md = Markdown(app, extensions=['fenced_code'])


@app.template_filter('datetime')
def format_datetime(value):
    date = datetime.fromtimestamp(value)
    return date.strftime("%d %B, %Y %H:%M:%S")


@app.route('/', methods=['GET', 'POST'])
def index():
    twitter = TwitterClient()
    loc = None
    if request.method == 'POST' and request.form.get('location'):
        radius = request.form.get('radius')
        loc = request.form.get('location')
        tweets = twitter.search_tweets(loc, radius)
    else:
        tweets = twitter.search_tweets()
    reddit = RedditClient()
    posts = reddit.get_hot_posts()
    return render_template('index.html', tweets=tweets, reddit=posts, area=loc)