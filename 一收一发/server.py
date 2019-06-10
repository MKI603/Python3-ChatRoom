# -*-coding:utf-8-*-
import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 11111

serversocket.bind((host,port))
serversocket.listen(1)
clientsocket,addr = serversocket.accept()


while True:
    data = clientsocket.recv(1024).decode('utf-8')
    print(data)
    user_input = input('>>>')
    clientsocket.send(user_input.encode('utf-8'))

    # clientsocket.close()
serversocket.close()



# netstat -ano | findstr xxxx
# taskkill /pid xxxx /f 