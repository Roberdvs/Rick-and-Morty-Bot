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
    twt = api.search(q="Rick and Morty", rpp= 10)

#list of specific strings we want to check for in Tweets

    for s in twt:
        sn = s.user.screen_name
        rdm=random.randint(0, len(quotes) -1) #Numero aleatorio de quote
        m = "@%s " % (sn) + quotes[rdm]
        if len(m)>140:                      #Si user + mensaje supera 140 caracteres le damos otra oportunidad de frase.
            rdm=random.randint(0, len(quotes) -1) #Numero aleatorio de quote
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
                s = api.update_status(status=m, in_reply_to_status_id=s.id)
            except tweepy.TweepError as e:
                print (e)
            time.sleep(200)
