import json
import tweepy
from tweepy import OAuthHandler

# Authorise our app to use Twitter.
# Consumer key and secret authenticate requests to Twitter platform.
# Access token is used to make API requests on your own account's behalf.
consumer_key    = '8GPTRMG6uPINXpze1ZEybc3Rm'
consumer_secret = 'h7bmj45qtxywjV23enwKrXB18D46cec6Wcncu6zxajgWM8OeIZ'
access_token    = '525359502-Slia9aBQwQdijrq2iNPEORDoNiUBEuyV1No0I6Wh'
access_secret   = '3p3sPcmeQ5a0VJ9tgSxpeBhg65h06RqYDnQbCz7b0h3fD'

# Create an OAuthHandler instance
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Download 10 home timeline tweets and print to console
for status in tweepy.Cursor(api.home_timeline).items(10):
  # Process a single status
  print(status.text)

# Print JSON one tweet per line
def process_or_store(tweet):
  print(json.dumps(tweet))

# Process / store JSON
for status in tweepy.Cursor(api.home_timeline).items(10):
  process_or_store(status._json)

# Find a list of your followers
for friend in tweepy.Cursor(api.friends).items(10):
  process_or_store(friend._json)

# List your tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
  process_or_store(tweet._json)
