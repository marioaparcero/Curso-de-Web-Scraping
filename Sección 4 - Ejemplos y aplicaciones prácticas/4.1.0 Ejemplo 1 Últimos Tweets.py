%run "oauth.py"
# Aquí introducimos nuestras claves de Twitter
def oauth() :
    return { "consumer_key" : "XXXX",
        "consumer_secret" : "XXXX",
        "token_key" : "XXXX",
        "token_secret" : "XXXX" }
# Esta función va a generar los parámetros necesarios para generar la URL
def augment(url, parameters) :
    secrets = oauth()
    consumer = OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = OAuthToken(secrets['token_key'],secrets['token_secret'])

    oauth_request = OAuthRequest.from_consumer_and_token(consumer, 
        token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()

import urllib.request
import json

#https://developer.twitter.com/en/docs/api-reference-index
#https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline
TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

acct = 'openwebinars'
n_tweets = 5

url = augment(TWITTER_URL,
             {'screen_name':acct, 'count': n_tweets,'include_rts':'True',
             'tweet_mode':'extended'})

connection = urllib.request.urlopen(url)

data = connection.read().decode()
js = json.loads(data)

for k in range(0,n_tweets):
    tweet = js[k]['full_text']
    print('\nTweet ' + str(k+1) + ': '+ tweet)