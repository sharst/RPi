from bluetooth import BluetoothSocket, RFCOMM, discover_devices


class BluetoothConnection(object):
	def __init__(self):
		self.client_socket = None
		self.server_socket = None
		self.connected = False
		
	
	def createServer(self, port = 3):
		self.server_socket=BluetoothSocket( RFCOMM )

		self.server_socket.bind(("", port))
		self.server_socket.listen(1)

		print "Trying to connect.."
		self.client_socket, _ = self.server_socket.accept()
		print "Connected!"
		
		self.connected = True
		
	def createClient(self, address, port = 3):
		if address == "first":
			address = self.searchDevices()[0]
		self.client_socket=BluetoothSocket( RFCOMM )
		print "Trying to connect.."
		self.client_socket.connect((address, port))
		print "Connected!"
		self.connected = True
	
	def searchDevices(self):
		return discover_devices()
		
	def receiveData(self, bufsize = 1024):
		if self.connected:
			return self.client_socket.recv(bufsize)
		else:
			print "Not yet connected!"
	
	def sendFile(self, filename):
		f = open(filename, 'r')
		data = f.readlines()
		for line in data:
			self.sendData(line)
		f.close()
	
	def receiveFile(self, filename, bufsize = 4096):
		data = self.receiveData(bufsize)
		f = open(filename, 'w')
		f.writelines(data)
		f.flush()
		f.close()
		
	def sendData(self, data):
		if self.connected:
			self.client_socket.send(data)
			
	def closeConnection(self):
		if self.server_socket is not None:
			self.server_socket.close()
		
		self.client_socket.close()
		
		self.connected = False