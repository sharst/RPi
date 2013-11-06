import socket


class WifiConnection(object):
    def __init__(self):
        self.client_socket = None
        self.server_socket = None
        self.connected = False
        
    
    def createServer(self, port = 3):
        self.server_socket=socket.socket()
        self.server_socket.bind(("", 5000))
        self.server_socket.listen(1)
        
        print "Trying to connect.."
        self.client_socket, address = self.server_socket.accept()
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        
        print "Connected! This server is now reachable at IP: "
        print repr(s.getsockname()[0])
        
        self.connected = True
        
    def createClient(self, address, port = 3):
        self.client_socket=socket.socket()
        print "Trying to connect.."
        self.client_socket.connect((address, port))
        print "Connected!"
        self.connected = True
    
        
    def receiveData(self, bufsize = 1024):
        if self.connected:
            return self.client_socket.recv(1024)
        else:
            print "Not yet connected!"
        
    def sendData(self, data):
        if self.connected:
            self.client_socket.send(data)
            
    def closeConnection(self):
        if self.server_socket is not None:
            self.server_socket.close()
        
        self.client_socket.close()
        
        self.connected = False