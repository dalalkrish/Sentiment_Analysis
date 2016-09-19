# -*- coding: utf-8 -*-
"""
Created on Fri May 27 21:53:59 2016

@author: Krishnang
"""
#Python_Script

import tweepy
import csv

consumer_key = "i5Q19ib8Scb1NjI7ICCQxQ9zb"
consumer_secret = "Mx4ISJn6MIWR2iciITs74STfK2z6SnfwabpwsJ0pShmYcWiv5z"
access_key = "122880215-IXKNFLwybA1wTkitUMDigsvc2FIVGOX8d5yQsyTj"
access_secret = "5S7QRw9RWddHTv1VZrivtrGAxqfbqCaWc741SlBzFPcry"

def get_tweets(username):
    
    initialize = tweepy.OAuthHandler(consumer_key, consumer_secret)
    initialize.set_access_token(access_key, access_secret)
    api = tweepy.API(initialize)

    down_tweets = []
    
    class StreamListener(tweepy.StreamListener):
        def on_status(self, tweet):
            print 'Ran on_status'

        def on_error(self, status_code):
            print 'Error: ' + repr(status_code)
            return False

        def on_data(self, data):
            print data


    l = StreamListener()
    streamer = tweepy.Stream(auth = initialize, listener=l)
    setTerms = ['Marjiuana', 'Weed', 'ganja']
    streamer.filter(locations = [-125.0011, 24.9493, -66.9326, 49.5904], track = setTerms)
    
    new_tweets = api.user_timeline(screen_name = username, count = 10)
    
    down_tweets.extend(new_tweets)
    
    old_tweet = down_tweets[-1].id - 1
    
    while len(new_tweets) > 0:
        
        new_tweets = api.user_timeline(screen_name = username, count = 10, max_id = old_tweet)
        down_tweets.extend(new_tweets)
        old_tweet = down_tweets[-1].id - 1
        
    final_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in down_tweets]
    
    #with open('%s_tweets.csv' %username, 'wb') as f:
    #    writer = csv.writer(f)
    #    writer.writerow(["id","created_at","text"])
    #    writer.writerows(final_tweets)
    
    pass


if __name__ == '__main__':
    get_tweets('krish051290')
            

    
    
    
    
    

