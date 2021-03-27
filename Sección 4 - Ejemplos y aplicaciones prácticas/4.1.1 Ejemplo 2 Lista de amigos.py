import urllib.request
import json

#https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-list
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

acct = input('Introduzca una cuenta de Twitter: ')
url = augment(TWITTER_URL,{'screen_name':acct, 'count':'10'})

connection = urllib.request.urlopen(url)
data = connection.read().decode()

js = json.loads(data)
#print(json.dumps(js, indent=2))

for u in js['users']:
    print(u['screen_name'])