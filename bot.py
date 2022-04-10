import tweepy
import time
import credentials as c
from generate_saying import getStanleySaying

# makes the auth object
auth = tweepy.OAuth1UserHandler(
   consumer_key = c.CONSUMER_KEY, 
   consumer_secret = c.CONSUMER_SECRET, 
   access_token = c.ACCESS_TOKEN, 
   access_token_secret = c.ACCESS_TOKEN_SECRET
)

# accesses api
api = tweepy.API(auth, wait_on_rate_limit=True)

INTERVAL = 60 * 6 * 6 # 6 hours for testing

# main code
while True:
   print("tweeting...")
   api.update_status(status = getStanleySaying())
   print("sleeping...")
   time.sleep(INTERVAL)

