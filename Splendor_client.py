import socket               # Import socket module

s = socket.socket()         # Create a socket object

host = socket.gethostname() # Get local machine name
if (host != "FW-CodingLaptop"):         #  Just for testing, running server on my laptop
     host = "73.71.247.208"  # Our house's IP address seen from outside
port = 61111                # Reserve a port for your service.

s.connect((host, port))
print("I am " + host + ", I received message " + s.recv(1024).decode('ascii'))
s.close()