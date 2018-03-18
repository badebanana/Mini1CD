"""
 Implements a simple socket server

"""

import socket


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

# Print message from client
msg = client_connection.recv(1024).decode()
print('Client_Connection Received:', msg)

"""
while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()
    while True:
        # Print message from client
        msg = client_connection.recv(1024).decode()
        if msg == "exit":
            break
        try:
            evalmsg = str(eval(msg))
            print(msg, '=', evalmsg)
            print('Client_Connection Received:', msg)
            client_connection.send(msg.encode())
        except:
            client_connection.send("Tá mal".encode())
"""
# Close client connection
client_connection.close()

# Close socket
server_socket.close()