import tweepy
import time
# import credentials as c
from generate_saying import getStanleySaying
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

# makes the auth object - V1 FOR TESTING
# auth = tweepy.OAuth1UserHandler(
#    consumer_key = c.CONSUMER_KEY, 
#    consumer_secret = c.CONSUMER_SECRET, 
#    access_token = c.ACCESS_TOKEN, 
#    access_token_secret = c.ACCESS_TOKEN_SECRET
# )

# makes the auth object - V2 FOR DEPLOYMENT
auth = tweepy.OAuth1UserHandler(
   consumer_key = CONSUMER_KEY, 
   consumer_secret = CONSUMER_SECRET, 
   access_token = ACCESS_TOKEN, 
   access_token_secret = ACCESS_TOKEN_SECRET
)

# accesses api
api = tweepy.API(auth, wait_on_rate_limit=True)

INTERVAL = 60 # * 6 * 6 # 6 hours for testing

# main code
while True:
   print("tweeting...")
   api.update_status(status = getStanleySaying())
   print("sleeping...")
   time.sleep(INTERVAL)

