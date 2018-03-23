"""
 Implements a simple socket server

"""

import socket

import json

from Functions import*

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

# Wait for client connections
client_connection, client_address = server_socket.accept()

msg = client_connection.recv(1024).decode()
dic = json.loads(msg)

val = []
for i in functions:
    if dic['method'].upper() == i.upper():
        val.append(int(dic['params']['x']))
        val.append(int(dic['params']['y']))
print(add(val))

# Print message from client
#print('Client_Connection Received:', msg)

# Close client connection
client_connection.close()

# Close socket
server_socket.close()