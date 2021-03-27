import urllib.request
import json

url1 = 'https://api.openaq.org/v1/cities'

pais = input('Introduzca las siglas del país (por ejemplo ES): ')

url2 = url1 + '?country=' + pais

datos = urllib.request.urlopen(url2).read().decode()
#print(datos)

js = json.loads(datos)

for k in range(50):
    city = js['results'][k]['city']
    print(city)