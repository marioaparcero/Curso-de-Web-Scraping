#Para extraer datos de una web tenemos que analizar el código fuente. Si inspeccionamos el valor del fondo vemos que tiene esta etiqueta:

#<td class="line text">EUR 15.15</td>
#Por lo tanto, voy a utilizar BeautifulSoup para extraer las etiquetas "td" con class = "line text"

import urllib
from bs4 import BeautifulSoup
#iShares Dev Rl Ett Idx (IE) Instl Acc €
participaciones = 50 # Estas son mis participaciones en el fondo de inversión
url= 'http://www.morningstarfunds.ie/ie/funds/snapshot/snapshot.aspx?id=F00000PJME'
html=urllib.request.urlopen(url)
soup=BeautifulSoup(html)
tags = soup.find_all("td",class_="line text") # Extraigo las etiquetas 
valor = float(tags[0].contents[0].replace('EUR\xa0','')) # Me quedo únicamente con el valor numérico
total = participaciones * valor
print(total)
#849.0