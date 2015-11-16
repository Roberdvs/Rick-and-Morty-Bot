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
api = tweepy.API(auth, proxy="proxy.server:3128")
while(1):
    twt = api.search(q="Rick and Morty", count=1, result_type="recent")
    time.sleep(30)
#twt = tweepy.Cursor(api.search, q="Rick and Morty", count=8, result_type="recent", include_entities=True).items()
    n=0
    for s in twt:
        n=n+1
        sn = s.user.screen_name
        rdm=random.randint(0, len(quotes) -1) #Numero aleatorio de quote
        try:
            m = "@%s " % (sn) + quotes[rdm]
            if len(m)>140:                      #Si user + mensaje supera 140 caracteres le damos otra oportunidad de frase.
                rdm=random.randint(0, len(quotes) -1) #Numero aleatorio de quote
                m = "@%s " % (sn) + quotes[rdm]
            print (m)
        except:
            continue
#            rdm=random.randint(0, len(quotes) -1) #Numero aleatorio de quote
#            m = "@%s " % (sn) + quotes[rdm]
        filename=open('history.txt','r')
        historial=filename.read()
        filename.close()
        if sn not in historial:             #Si el usuario no esta en el historial podemos enviar el tweet
            filename=open('history.txt','a')
            filename.write(sn)
            filename.close
            try:
                s = api.update_status(status=m, in_reply_to_status_id=s.id)
            except tweepy.TweepError as e:
                print (e)
        time.sleep(3630)
        if n==20:
            open('history.txt', 'w').close() #Borrar el contenido del fichero historial de usuarios