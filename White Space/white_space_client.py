import socket

server_ip = '127.0.0.1'
server_port = 11111

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

try:
    input = input("Enter input: (spaces/tabs) ")
    client_socket.sendall(input.encode())

finally:
    client_socket.close()
