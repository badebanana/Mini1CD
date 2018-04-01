import socket
import json
from ClientTest import*

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send message
while True:
    msg = msgUser()
    file_json = fileJson(msg)
    client_socket.send(json.dumps(file_json).encode())

    msgResult = client_socket.recv(1024).decode()
    dic = json.loads(msgResult)
    print(dic['result'])
    if dic['result'] == 'Até à próxima':
        # Close socket
        client_socket.close()

# Close socket
client_socket.close()
