import urllib.request

fhand = urllib.request.urlopen('https://www.w3.org/TR/PNG/iso_8859-1.txt')
for line in fhand:
    print(line.decode().strip())