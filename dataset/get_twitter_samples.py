import json
from nltk.corpus import twitter_samples

my_json = twitter_samples.open("negative_tweets.json").read().split("\n")
c = 0
s = ""
for tweet_data in my_json:
    try:
        tweet = json.loads(tweet_data)
        c += 1
    except:
        continue
    s = tweet['text'] + "\n" + s

    #print(tweet['text'])
with open("twitter_neg1.txt", "w") as f:
    f.write(s)
print("Number of tweets added: %d" %c)
