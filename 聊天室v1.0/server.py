#-*-utf8-*-
import sys
import socket
import threading

class Server():
	def __init__(self):
		print('Server start.....')
		self.clients = list()
		self.host = socket.gethostname()
		self.port = 11111

	def start(self):
		"""
		绑定socket，并且开启监听
		"""
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		addr = (self.host, self.port)
		s.bind(addr)
		s.listen(10)

		while True:
			c, addr = s.accept()
			print(str(addr) + 'someone connected....')
			self.clients.append(c)
			t = threading.Thread(target=self.Receive, args=(c,))
			t.start()
		s.close()

	def Receive(self, c):
		"""
		监听模块
		"""
		while True:
			Data = c.recv(1024).decode('utf-8')
			Data = eval(Data)
			print(Data['name'] + ':' + Data['data'])
			self.Send(c, str(Data))

	def Send(self, c, Data):
		"""
		发信模块
		"""
		Data = Data.encode('utf-8')
		for c in self.clients:
			c.send(Data)


if __name__ == "__main__":
	server = Server()
	server.start()