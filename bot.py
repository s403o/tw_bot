import time
import os
import tweepy as tw

#login to tw acc api
auth = tw.OAuthHandler(consumer_key = "", consumer_secret = "")
auth.set_access_token(access_token = "", access_secret = "")
api = tw.API(auth)

#iterates imgs from folder
os.chdir('imgs')
for image in os.listdir('.'):
  api.update_with_media(image)
  time.sleep(10)