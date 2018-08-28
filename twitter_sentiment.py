#sentiment analysis is the practice of underdstanding and extracting feelings from data
#enter your own consumer_key, consumer_secret, access_token, access_token_secret for accessing your own twitter account
#access_token, access_token_secret shall be found out by creating your own App in your own twitter account and this access_token shall help us access the API provided by twitter


import tweepy
from textblob import TextBlob

consumer_key = '' #enter your own consumer_key(from twitter account)
consumer_secret = '' #enter your own consumer_secret

access_token = '' #enter your own access token 
access_token_secret = '' #enter your own access token secret

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('atal bihari bajpayee')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
#in the analyses printed, we get 2 measures: polarity measures how positive or negative some tweet may be and subjectivity measures how much biased or factual a tweet is
