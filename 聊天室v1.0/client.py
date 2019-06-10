#-*-utf8-*-
import socket
import threading
import sys

class Client():
    def __init__(self):
        """
        初始化 获取用户信息
        """
        self.host = socket.gethostname()
        self.port = 11111

        self.Username = input('please input username:')
        self.Information = {
            'name' : self.Username
        }

    def start(self):
        """
        绑定socket， 开启监听
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (self.host, self.port)
        s.connect(addr)

        t = threading.Thread(target=self.send, args=(s,))
        t.start()

        while True:
            Data = s.recv(1024).decode('utf8')
            Data = eval(Data)
            print('\n' + Data['name'] + ':' + Data['data'])

        s.close()
        
    def send(self,c):
        """
		发信模块
		"""
        while True:
            data = input('$' + self.Username + '>>>').strip()
            self.Information['data'] = data
            c.send(str(self.Information).encode('utf8'))

if __name__ == "__main__":
    client = Client()
    client.start()
    
