import ssl
import socket
import pathlib

def handle_connection(conn):
    conn.settimeout(5)
    
    # Server side mutual authentication
    server_certfile = 'server.crt'
    server_keyfile = 'server.key'
    client_cafile = 'client.crt'

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, cafile=client_cafile)
    context.load_cert_chain(certfile=server_certfile, keyfile=server_keyfile)

    secure_conn = context.wrap_socket(conn, server_side=True)

    try:
        data = secure_conn.recv(1024)
        print(f"Received: {data.decode()}")
        secure_conn.sendall(b"Hello, client!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        secure_conn.close()

if __name__ == "__main__":
    server_certfile = 'server.crt'
    server_keyfile = 'server.key'
    client_certfile = 'client.crt'
    client_keyfile = 'client.key'

    # Generate self-signed certificates (Replace with actual certificates in a production environment)
    pathlib.Path(server_certfile).write_text("server certificate content here")
    pathlib.Path(server_keyfile).write_text("server private key content here")
    pathlib.Path(client_certfile).write_text("client certificate content here")
    pathlib.Path(client_keyfile).write_text("client private key content here")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server started, waiting for connections...")
    
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            handle_connection(client_socket)
    except KeyboardInterrupt:
        print("Server stopped")
    finally:
        server_socket.close()
