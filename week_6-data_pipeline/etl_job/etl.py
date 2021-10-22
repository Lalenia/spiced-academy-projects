import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()

time.sleep(10)

pg = create_engine('postgresql://postgres:postgres@postgresdb:5432/tweets', echo=True)
pg.execute('''
    CREATE TABLE IF NOT EXISTS brit_tweets (
    text VARCHAR(500),
    score NUMERIC
);
''')

client = pymongo.MongoClient(host="mongodb",
                             port=27017,
                             username="lali",
                             password="lale",
                             authSource="admin")

db = client.tweets

collection = db.tweet_data

entries = collection.find()

for e in entries:
    print(type(e))
    sentiment = s.polarity_scores(e['text'])
    print(sentiment)
    #Convert all emojis in the texts into Ascii characters
    #for string in tweet_dict:
    #e = deEmojify(x)
    score = sentiment['compound']
    text = e['text']
    query = "INSERT INTO brit_tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))
    


