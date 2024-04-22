import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"[*] Server started on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[*] Connection from {addr}")

        message = "Hello, client!"
        client_socket.send(message.encode())

        client_socket.close()

if __name__ == '__main__':
    server_program()
