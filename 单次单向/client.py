# -*-coding:utf-8-*-
import sys
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 11111

s.connect((host, port))

msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))