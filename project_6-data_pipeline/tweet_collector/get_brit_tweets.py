import config
from tweepy import OAuthHandler, Cursor, API
from tweepy.streaming import StreamListener
import logging
import pymongo

client = pymongo.MongoClient(host="mongodb",
                             port=27017,
                             username="lali",
                             password="lale",
                             authSource="admin")
db = client.tweets
collection = db.tweet_data

def authenticate():

    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    return auth

if __name__ == '__main__':
    auth = authenticate()
    api = API(auth)

    cursor = Cursor(
        api.user_timeline,
        id = 'britneyspears',
        tweet_mode = 'extended'
    )

    for status in cursor.items(10):
        text = status.full_text

        # take extended tweets into account
        if 'extended_tweet' in dir(status):
            text =  status.extended_tweet.full_text
        if 'retweeted_status' in dir(status):
            r = status.retweeted_status
            if 'extended_tweet' in dir(r):
                text =  r.extended_tweet.full_text

        tweet = {
            'text': text,
            'username': status.user.screen_name,
            'followers_count': status.user.followers_count
        }
        
        collection.insert_one(tweet)
        
        
        print(tweet)