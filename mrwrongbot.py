import os
import sys
import json
import urllib
import random
import tweepy
import time

jsonurl = urllib.urlopen("http://hypem.com/playlist/popular/noremix/json/1/data.js")
#REPLACE WITH OTHER JSON IF DESIRED
text = json.loads(jsonurl.read())
n=str((random.randrange(0,10)))
#CAN INCREASE LATTER NUMBER IF WANT TO TAKE FROM TOP 20, 50, ETC.
artist=text[n]["artist"]
filename=open("YOUR_TEXT_FILE", 'r')
f=filename.readlines()
filename.close()
n=(random.randrange(0,8))*2
#THE LATTER NUMBER SHOULD=THE TOTAL NUMBER OF INSULTS + 1;
#EACH INSULT SHOULD BE SPLIT ACROSS TWO LINES, WITH THE ARTIST NAME INSERTED AT THE LINE BREAK
x = str.strip(f[n])
if x == "":
    x=x
else:
    x =  x + " "
y = str.strip(f[n+1])
if y == "":
    y=y
else:
    y =  " " + y
z = x + artist + y
print z
print len(z)

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(z)
 
