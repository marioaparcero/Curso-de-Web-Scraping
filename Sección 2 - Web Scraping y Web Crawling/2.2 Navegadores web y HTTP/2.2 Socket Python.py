import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.w3.org', 80))
cmd = 'GET https://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\\r\\n\\r\\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode()) #,end='')

mysock.close()