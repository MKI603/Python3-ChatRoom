# -*-coding:utf-8-*-
import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 11111

serversocket.bind((host,port))
serversocket.listen(1)

while True:
    clientsocket,addr = serversocket.accept()
    print("somebody come %s" % str(addr))
    msg = "hello " + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
serversocket.close()
# netstat -ano | findstr xxxx
# taskkill /pid xxxx /f 