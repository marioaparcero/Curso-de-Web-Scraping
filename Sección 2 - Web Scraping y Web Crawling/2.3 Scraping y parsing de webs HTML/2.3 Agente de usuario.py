import urllib.request
from bs4 import BeautifulSoup
url = 'https://platzi.com/'
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
f = urllib.request.urlopen(req)
soup = BeautifulSoup(f.read().decode('utf-8'))
tags = soup.find_all("a")
print(tags) 