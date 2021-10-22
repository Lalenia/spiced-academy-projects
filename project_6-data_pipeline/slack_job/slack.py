from numpy.lib.histograms import _search_sorted_inclusive
import requests
import time
#import config
import pandas as pd
from emoji import deEmojify
from sqlalchemy import create_engine

#webhook_url = config.WH_URL
webhook_url = "https://hooks.slack.com/services/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"

time.sleep(15)

#create connection with postgres.
pg = create_engine('postgresql://postgres:postgres@postgresdb:5432/tweets', echo=True)

#request britney's tweets from the database and save them to a file.
df_brit = pd.read_sql_query('select * from brit_tweets ORDER BY score DESC LIMIT 1', pg)

#prepare data for the slack bot, by converting emojis to Ascii characters.
df_brit['text'] = df_brit['text'].apply(lambda x: deEmojify(x))


def show_tweet_in_slack():   
    for tweet , score in df_brit.items():
        tweet = df_brit['text']
        score  = df_brit['score']

    msg=f"*LATEST :cat:BRITNEY'S:cat: TWEET*\n:mega: {tweet}\n:dart: Sentiment score : {score}\n:soon: Next tweet will come in 15 seconds..."

    data = {'blocks': [
            {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Britney's Tweets. #FreeBritney*" + msg
                #"text": msg

         
            },
            "accessory": {
                "type": "image",
                "image_url": "https://media1.faz.net/ppmedia/aktuell/3394372010/1.7232299/width610x580/free-britney-demonstranten-im.jpg",
                "alt_text": "tweeter"
            },
            
            }]
        }

    return requests.post(url=webhook_url, json=data)

show_tweet_in_slack()
#time.sleep(20)
