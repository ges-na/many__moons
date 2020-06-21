import tweepy
from moon_twitter import *
from environs import Env
# import ipdb
 
env = Env()
env.read_env()

consumer_key = env.str('CONSUMER_KEY')
consumer_secret = env.str('CONSUMER_SECRET')
access_token = env.str('ACCESS_TOKEN')
access_secret = env.str('ACCESS_SECRET')
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

status = generate_moon()


api.update_status(status)
