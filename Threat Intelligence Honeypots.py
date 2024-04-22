import socket
import threading

def start_honeypot(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(5)
        print(f"Honeypot started on port {port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            
            # Log connection information and data
            data = client_socket.recv(1024)
            print(f"Received data: {data.decode()}")
            
            # Add threat intelligence analysis here
            
            client_socket.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    port = 8080  # Replace with the desired port number
    start_honeypot(port)
