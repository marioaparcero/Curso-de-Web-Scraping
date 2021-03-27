#Extraemos los hashtags de los próximos encuentros
url = 'http://www.laliga.es'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)

tags = soup.find_all("a",class_="hashtag big2")

hashtags = list()

for tag in tags:
    hashtags.append(tag.contents[0])
print(hashtags)