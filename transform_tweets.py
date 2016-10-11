#!/usr/bin/env python


import sys
import re
for line in sys.stdin:
	data = line.split("\t")
	tweet_id,tweet,tweet_location = data
	tweet1 = re.sub(r"http\S+", "", tweet)
	tweet2 = tweet1.replace("'", "")
	tweet3 = re.sub('[^A-Za-z0-9]+', ' ', tweet2)
	if ',' in tweet_location:
		tweet_location = tweet_location.split(",")
	else:
		tweet_location = tweet_location.replace(" ", ",")
		tweet_location = tweet_location.split(",")
	area,state = tweet_location
	state = state.strip()
	if state == 'USA' :
		print '%s\t%s\t%s' % (tweet_id,tweet3,area)
	else:
		print '%s\t%s\t%s' % (tweet_id,tweet3,state)
