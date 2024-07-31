import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs

from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Access variables
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')                             # Access Key
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')               # Access secret
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')                   # Consumer key
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')     # Consumer secret

# Twitter authentication
auth = tweepy.OAuth1UserHandler(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET_KEY,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

# Creating an API object
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@arunp77_',
                           # 200 is the maximum allowed count
                           count =200,
                           include_rts=False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                            tweet_mode='extended')

print(tweets)
