import hashlib
import os
import socket

# Receiver details
server_ip = 'localhost'
server_port = 12345  # Use the same port as in the sender script
output_directory = '***'  # Replace with the directory to save received files

def calculate_hash(data):
    """Calculate the hash of binary data."""
    hasher = hashlib.sha256()
    hasher.update(data)
    return hasher.hexdigest()

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the server address and port
    server_socket.bind((server_ip, server_port))
    
    # Listen for incoming connections
    server_socket.listen(1)  # Allow only one client to connect at a time
    
    print(f"Listening on {server_ip}:{server_port}...")
    
    # Accept a connection from a sender
    sender_socket, sender_address = server_socket.accept()
    print(f"Accepted connection from {sender_address}")
    
    while True:
        # Receive binary data from the sender
        data = sender_socket.recv(65536)  # Receive in 64KB chunks
        
        if not data:
            break
        
        # Calculate the hash of the received data
        received_hash = calculate_hash(data)
        
        # Save the received data to a file
        file_name = f"{received_hash}.bin"
        file_path = os.path.join(output_directory, file_name)
        
        with open(file_path, 'wb') as file:
            file.write(data)
    
    # Close the sockets
    sender_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
