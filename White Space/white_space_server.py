import socket

server_ip = '127.0.0.1'
server_port = 11111 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1) 

print(f"Listening on {server_ip}:{server_port}")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

try:
    received_data = client_socket.recv(256).decode()
    covert_data = received_data.replace(' ', '0').replace('\t', '1')
    print(f"Received data: {covert_data}")
    
finally:
    client_socket.close()
    
server_socket.close()
