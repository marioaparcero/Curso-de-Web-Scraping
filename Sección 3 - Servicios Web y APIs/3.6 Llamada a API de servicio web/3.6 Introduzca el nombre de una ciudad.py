import urllib.request
import json
ciudad = input('Introduzca el nombre de una ciudad ')

url1 = 'https://api.openaq.org/v1/latest'

url2 = url1 + '?limit=1&city=' + ciudad

data = urllib.request.urlopen(url2).read().decode()

js = json.loads(data)
parameter = js['results'][0]['measurements'][1]['parameter']
valor = js['results'][0]['measurements'][1]['value']
unidades = js['results'][0]['measurements'][1]['unit']

print('El valor de ',parameter,' en', ciudad, 'es de ',valor,unidades)