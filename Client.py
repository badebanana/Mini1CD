"""
 Implements a simple socket client

"""

import socket

import json

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send message
msg = input("> ")

file_json = {
    "id": 0,
    "method": msg[0:3],
    "jsonrpc": "2.0",
    "params": {"x":msg[3], "y":msg[4]},
}
client_socket.send(json.dumps(file_json).encode())

# Close socket
client_socket.close()