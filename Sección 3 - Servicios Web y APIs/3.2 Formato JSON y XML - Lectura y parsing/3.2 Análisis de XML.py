import urllib.request
import xml.etree.ElementTree as ET

url = 'https://www.w3schools.com/xml/cd_catalog.xml'

## Vamos a leer el archivo XML de la web https://www.w3schools.com/xml/cd_catalog.xml 
data = urllib.request.urlopen(url).read()
## y parsearlo con la librería ElementTree
tree = ET.fromstring(data.decode())

lst = tree.findall('CD')
print('Número de registros:', len(lst))

for item in lst:
    print('\r')
    print('Titulo:', item.find('TITLE').text)
    print('Artista:', item.find('ARTIST').text)
    print('Precio:', item.find('PRICE').text)
    
## Al llamar a fromstring convertimos la representación del XML de string a un "árbol". 
## En este formato de árbol, disponemos de diversos métodos con los que podemos extraer partes del XML. 
## Por ejemplo, la función find busca en el XML y devuelve el elemento que coincide con la etiqueta especificada.