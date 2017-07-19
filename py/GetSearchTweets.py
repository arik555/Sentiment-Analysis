#!/usr/bin/env python3

import tweepy
from tweepy import OAuthHandler
from tweepy.parsers import JSONParser


def get_search_tweets(search_topic, tweet_count):
    consumer_key = "Y7CBeJsqQtXhxX75fw5gj"
    consumer_secret = "FQLVJQgfG5lO8vX8VUU8Qxq5PZDFSFh2Op3SIYRLo0gmH"
    access_token = "8064-tz55Z6hattbypRe0kOTWTZDEu58mYswq0OPtP4B"
    access_token_secret = "lZBVph4pEatnnsNrZJoVW8J1TrzZ6dKDeKOP6"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=JSONParser())
    
    res_json = api.search(q=search_topic, lang="en", count=tweet_count)
    for res in res_json['statuses']:
        with open("tweets/twitter.txt", "a", encoding="utf_16") as f:
            f.write(res['text'].replace("\n", " ") + "\n")
        print(res['text'])
        print("--------------------------------")
