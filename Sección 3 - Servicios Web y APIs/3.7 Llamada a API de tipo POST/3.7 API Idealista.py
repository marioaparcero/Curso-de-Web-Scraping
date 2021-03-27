import json
import requests
from requests.auth import HTTPBasicAuth

idealista_url = "https://api.idealista.com/oauth/token"
r = requests.post(idealista_url,
                  auth=HTTPBasicAuth("9imfkl9ugl3ofiv9b95i7am1w98yzpu7", "8nZfatljCytZ"),
                  data={"grant_type": "client_credentials"})
print(r.text)
token_response = json.loads(r.text)
token_value = token_response["access_token"]
print("Token: " + token_value)

country = 'es'
center = '40.42938099999995,-3.7097526269835726'
numPage = '1'
distance = '1000'
propertyType = 'homes'
operation = 'rent'

api_url = "http://api.idealista.com/3.5/es/search?center="+center+"&country="+country+"&distance="+distance+"&propertyType="+propertyType+"&operation="+operation
print(api_url)

#r = requests.post(api_url,headers = {"Authorization": "Bearer " + token_value})
#js = json.loads(r.text)
#js
headers = {"Authorization": "Bearer " + token_value}
r = requests.post(api_url, headers=headers)
#print(r.text)
search_json = r.text
search_response = json.loads(search_json)
search_pretty = json.dumps(search_response, indent=4, sort_keys=True)
print(search_pretty)