#sentiment analysis is the practice of underdstanding and extracting feelings from data
#enter your own consumer_key, consumer_secret, access_token, access_token_secret for accessing your own twitter account
#access_token, access_token_secret shall be found out by creating your own App in your own twitter account and this access_token shall help us access the API provided by twitter


import tweepy
from textblob import TextBlob

consumer_key = 'ZH4lMaYKXhHBJ7WNe9XlAj1xC'
consumer_secret = 'yH9itMrpEYDNJbEKZdmYBSHFA9kYURj75sVZnAChU7BflnaPbX'

access_token = '466652775-bevQe4cPYVPSNjxn0kawVYmvkFd5UR3JkMBpfb4F'
access_token_secret = 'kM74Gu2coGIoNo38uANrgYCUTKvLdg29OsC0YnhtOx1iG'

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('atal bihari bajpayee')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
#in the analyses printed, we get 2 measures: polarity measures how positive or negative some tweet may be and subjectivity measures how much biased or factual a tweet is