import urllib.request
from bs4 import BeautifulSoup
url = 'https://tkambio.com/?gclid=Cj0KCQjwu6fzBRC6ARIsAJUwa2QXb7YtrSCklYY_H2tNpju2FOmxtBWffvJn46Bm_K-PDqjmQ61oChEaAlNEEALw_wcB&#39'
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
soup = BeautifulSoup(f.read().decode('utf-8'))
soup('a')