#El objeto de BeautifulSoup acepta diversos parsers:
   #html.parser (este parser no funciona en versiones antiguas de Python)
   #lxml (funciona más rápidamente, generalmente es la mejor elección)
   #html5lib (es más lento, pero más indulgente con HTML mal construidos)
#Si no especificas ninguno, se utiliza lxml por defecto.

# Instalación de la librería
import sys
!{sys.executable} -m pip install beautifulsoup4

#En el siguiente ejemplo, vamos a parsear una entrada HTML y extraer los links utilizando la librería BeautifulSoup. 
#Utilizaremos urllib para leer la página y después BeautifulSoup para extraer los atributos href 
#de las etiquetas de tipo ancla (a)
import urllib
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)

# Extraigo las etiquetas de tipo <a>
tags = soup('a')
for tag in tags:
    #print(tag.get('href'))
    #Mirar todas las partes de una etiqueta
    print('TAG:', tag)
    print('URL:', tag.get('href'))
    print('Contents:', tag.contents)
    print('Attrs:', tag.attrs)
    print('\n')