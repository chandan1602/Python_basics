import socket
import sys

'''
########################
#CONNECTING TO A SERVER#
########################
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Successfully created!!")
except socket.error as err:
    print("Socket creation failed with error: '%s'"%(err))
port=80
try:
    host_ip = socket.gethostbyname('www.google.com')
    print(host_ip)
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()
#connecting to the server
s.connect((host_ip, port))

print("The socket has successfully connected to google\non port == '%s'"%(host_ip))
'''

#create a socket object
s=socket.socket()
print("Socket successfully created")

#resolve a port on pc
port=12345

#Binding to the port.
#Not typed any ip in the ip field instead we have inputed an empty string
#which makes the server listen to the requests coming from another computers
#on the network
s.bind(('', port))
print("socket binded to '%s'"%(port))

#put the socket into listening mode
s.listen(5)
print("Socket is listening")

#a forever loop until we interupt it or an error occurs
while True:

    #Establish connection with the client
    c, addr = s.accept()
    print('Got connection from ', addr)

    #send a thankyou message to the client
    str="Thank you for connecting!"
    c.send(str.encode('ascii'))

    #close the cinnection with the client
    c.close()
