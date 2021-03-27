# Instalación de las librerías
import sys
!{sys.executable} -m pip install -U wordcloud

import urllib.request
import json

## https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline
TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

acct = 'openwebinars'
n_tweets = 200

RTS = input('¿Quiere tener en cuenta los retweets? (S/N) ')
if RTS == 'S': RTTS = 'True'
else: RTTS = 'False'


url = augment(TWITTER_URL,
             {'screen_name':acct, 'count': n_tweets,'include_rts':RTTS,
             'tweet_mode':'extended'})

connection = urllib.request.urlopen(url)

data = connection.read().decode()
js = json.loads(data)

print('Se han extraido los ', str(len(js)), ' tweets más recientes del usuario @', acct)

## Segunda parte
lista = []

for k in range(0,len(js)):
    tweet = js[k]['full_text']
    tweet2 = tweet.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    tweet3 = tweet2.split(' ')
    lista = lista + tweet3
    
preposiciones = ['ante','bajo','contra','desde','entre','hacia','hasta','para','segun','sobre','tras','como','este',
                 'esta','estos','estas','pero','porque','cuando','donde','quien']
                 
contadores = dict()
for palabra in lista:
    if len(palabra)>3 and palabra not in preposiciones:
        contadores[palabra]=contadores.get(palabra,0)+1
        

import pandas as pd
top_palabras=pd.DataFrame(list(contadores.items()),columns=['palabra','contador']).sort_values('contador',ascending=False)

top_palabras

#Por último, creamos la nube de palabras con ayuda de la librería wordcloud.
%matplotlib inline
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
text = top_palabras.values
wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    background_color = 'black',
    stopwords = STOPWORDS).generate(str(text))
fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()