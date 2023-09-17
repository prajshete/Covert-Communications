import os
import hashlib
import socket
import time

# Sender details
server_ip = 'localhost'
server_port = 12345 
directory_to_monitor = '***'  # Replace with the directory you want to monitor

def calculate_hash(file_path):
    """Calculate the hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64KB chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def main():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    
    while True:
        # Get a list of files in the directory
        files = os.listdir(directory_to_monitor)
        
        for file_name in files:
            file_path = os.path.join(directory_to_monitor, file_name)
            
            # Calculate the hash of the file
            file_hash = calculate_hash(file_path)
            
            # Send the file's binary content to the receiver
            with open(file_path, 'rb') as file:
                file_content = file.read()
                client_socket.send(file_content)
            
            # Sleep briefly to avoid rapid checking
            time.sleep(1)
    
if __name__ == "__main__":
    main()
