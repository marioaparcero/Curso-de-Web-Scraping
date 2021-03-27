import urllib
from bs4 import BeautifulSoup

url = 'http://www-math.mit.edu/~gs/'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)
tags = soup('a')
print('Enlaces en la página principal: \r\n')
for tag in tags:
    print(tag.contents[0],tag.get('href'))
    
print('\r\n Enlaces en las páginas secundarias: \r\n')
    
for tag in tags:
    newurl = tag.get('href',None)
    print('* Accediendo a los enlaces dentro de la página: ' + newurl)
    try:
        if newurl[0:4]=='http': html2 = urllib.request.urlopen(newurl)
        else: html2 = urllib.request.urlopen(url+newurl)
        soup2 = BeautifulSoup(html2)
        newtags = soup2('a')
        if len(newtags)>0:
            print(len(newtags),' enlaces:')
            for newtag in newtags:
                print(newtag.get('href'))
        else: print('No tiene más enlaces')
    except:
        print('No tiene más enlaces')