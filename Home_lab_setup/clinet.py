import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = client_socket.recv(1024)
    print(f"[*] Received from server: {message.decode()}")

    client_socket.close()

if __name__ == '__main__':
    client_program()
