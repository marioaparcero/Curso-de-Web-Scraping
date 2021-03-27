import urllib.request
from bs4 import BeautifulSoup
fondo = input('Selecciona el fondo que quieras consultar (A o B) y pulsa enter: ')
fondos_dic = {'A':'https://www.morningstar.es/es/funds/snapshot/snapshot.aspx?id=F0GBR04UOL',
'B':'https://www.morningstar.es/es/funds/snapshot/snapshot.aspx?id=F0GBR05WKI'}
url = fondos_dic[fondo]
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
tags = soup.find_all("td", class_="line text")
valor = float(tags[0].contents[0].replace(',','.').replace('\n','').replace('EUR\xa0',''))
print('El valor del fondo',fondo,'es',valor)