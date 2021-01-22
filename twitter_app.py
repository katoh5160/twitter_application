import tweepy
import time
from tqdm.notebook import tqdm
import re

CONSUMER_KEY        = ''
CONSUMER_SECRET_KEY = ''
ACCESS_TOKEN        = ''
ACCESS_TOKEN_SECRET = ''
SCREEN_NAME         = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

word_set = [""]
set_count = 100

for word in tqdm(word_set):
  results = api.search(q=word, lang="ja",count = set_count, result_type = "mixed")
  for result in tqdm(results):
      account_id   = result.user.screen_name
      account_name = result.user.name
      result_text  = result.text
      tweet_id     = result.id
      official_flag = result.user.verified
      result_follows   = result.user.friends_count
      result_followers = result.user.followers_count

      try :
          api.create_friendship(account_id)
          api.create_favorite(tweet_id)
          api.retweet(tweet_id)
          print("{0}：をフォローしました".format(account_name))
          time.sleep(1)
      except:
          continue
