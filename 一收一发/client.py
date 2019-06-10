# -*-coding:utf-8-*-
import sys
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 11111

s.connect((host, port))

while True:
    user_input = input('>>>').strip()
    s.send(user_input.encode('utf-8'))
    if len(user_input) == 0:
        s.close()
    reply = s.recv(1024).decode('utf-8')
    print(reply)



# msg = s.recv(1024)

# s.close()

# print(msg.decode('utf-8'))