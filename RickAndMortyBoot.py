#!/usr/bin/env python
import tweepy, time, random
#from our keys module (keys.py), import the keys dictionary
from keys import keys
## @BotRickAndMorty:tinyrick
## rickmortybot@gmail.com:tinyrick
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

filename=open('quotes.txt','r')
quotes=filename.readlines()
filename.close()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
while(1):
    twt = api.search(q="Rick and Morty")     
 
#list of specific strings we want to check for in Tweets
    t = ['rick and morty',
        'Rick and Morty']
    for s in twt:
        for i in t:
            if  i in s.text:
                sn = s.user.screen_name
                rdm=random.randint(0, len(quotes)) #Número aleatorio de quote
                m = "@%s " % (sn) + quotes[rdm]
                if len(m)>140:                      #Si user + mensaje supera 140 caracteres le damos otra oportunidad de frase.    
                    rdm=random.randint(0, len(quotes)) #Número aleatorio de quote
                    m = "@%s " % (sn) + quotes[rdm]
                print (m)
                
                filename=open('history.txt','r')
                historial=filename.read()
                filename.close()
                if m not in historial:
                    filename=open('history.txt','a')
                    filename.write(m)
                    filename.close
                    try:
                        s = api.update_status(m, s.id)
                        time.sleep(120)
                        break
                    except ValueError:
                        print ("Error sending the tweet")
                time.sleep(150)
    time.sleep(150)
time.sleep(1800)
