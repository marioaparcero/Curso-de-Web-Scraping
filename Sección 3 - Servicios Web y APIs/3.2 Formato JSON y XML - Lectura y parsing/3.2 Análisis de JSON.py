import json

## Vamos a leer el archivo data.json y parsearlo utilizando la librería json

f = open("data.json", "r")
info = json.loads(f.read())
## Con json.loads() se obtiene una lista la cual podemos recorrer con un bucle for, 
## donde cada elemento de la lista es un diccionario.

#print(json.dumps(info, indent=4, sort_keys=True))

print('Número de presidentes:', len(info))

for item in info:
    print('\r')
    print('Nombre:', item['nm'])
    print('Partido:', item['pp'])
    print('Años:', item['tm'])
