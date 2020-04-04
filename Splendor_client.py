import socket  # Import socket module

s = socket.socket()  # Create a socket object

port = 61111  # Reserve a port for your service.
server_local_name = 'FW-CodingLaptop'
server_remote_IP_addr = '73.71.247.208'
try:
    server_name = server_local_name
    s = socket.create_connection((server_local_name, port))
except:
    server_name = server_remote_IP_addr
    s = socket.create_connection((server_remote_IP_addr, port))

print("Server is '%s', I received message '%s'" % (server_name, s.recv(1024).decode('ascii')))
s.close()
