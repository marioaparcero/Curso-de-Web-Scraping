# Instalación de la librería pandas
import sys
!{sys.executable} -m pip install pandas

import urllib
from bs4 import BeautifulSoup
url = 'https://elpais.com/internacional/2018/01/31/actualidad/1517387619_036241.html'
html = urllib.request.urlopen(url)
soup2 = BeautifulSoup(html)
# Extraigo las etiquetas de tipo <p>
tags = soup2('p')
# Aquí guardo el discurso, inicialmente vacío
discurso = ''
for tag in tags:
    # Con esta condición filtro solo el texto que me interesa
    if (len(tag.attrs)) == 0:
        a= tag.contents[0] # Extraigo el contenido de la etiqueta
        discurso = discurso +  a # Voy concatenando cada contenido a la variable discurso

#print(discurso)
# Creo un diccionario para almacenar las palabras y contar las veces que aparece
contadores = dict()
# Elimino signos de (puntos, comas, etc.)
discurso = discurso.replace(',','').replace('.','').replace(':','').replace('?','').replace('(','').replace(')','')
# Paso todas las palabras a minúsculas (lower) y las corto palabra a palabra (split)
palabras = discurso.lower().split()
for palabra in palabras:
    # Añado al diccionario solo las palabras con más de 3 letras
    if len(palabra)>3:
        contadores[palabra] = contadores.get(palabra,0) + 1 
        
        
import pandas as pd
# Guardo las palabras en un dataframe ordenados de mayor a menor por el contador
pd.DataFrame(list(contadores.items()), columns=['palabra', 'contador']).sort_values('contador', ascending=False )