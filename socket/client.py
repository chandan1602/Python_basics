import socket
import sys

#Created a socket object
s=socket.socket()

#Resolving port
port=12345

#Connecting to the server on local computer
s.connect(('127.0.0.2', port))


#recieve data from server
print(s.recv(1024))

#closing the connection
s.close()
