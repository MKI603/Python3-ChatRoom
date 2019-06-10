# -*-coding:utf-8-*-
import socket
import sys
import threading

print("waitting......")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 11111

serversocket.bind((host,port))
serversocket.listen(2)
clientsocket,addr = serversocket.accept()
addr = str(addr)
print("connected by %s" %addr)

Flag = True
def receve(conn):
    global Flag
    while Flag:
        data = conn.recv(1024).decode('utf-8')
        if data == 'quit':
            Flag = False
        print("new message: %s" %data)
t1 = threading.Thread(target=receve, args=(clientsocket,))
t1.start()


while Flag: 
    user_input = input('>>>')
    clientsocket.send(user_input.encode('utf-8'))
    if user_input == 'quit':
        Flag = False


serversocket.close()


# while True:
#     data = clientsocket.recv(1024).decode('utf-8')
#     print(data)
#     user_input = input('>>>')
#     clientsocket.send(user_input.encode('utf-8'))

#     # clientsocket.close()
# serversocket.close()



# netstat -ano | findstr xxxx
# taskkill /pid xxxx /f 