import socket
import requests

def check_open_ports(target_host, target_ports):
    """Check for open ports on the target host."""
    open_ports = []
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def check_http_headers(url):
    """Check for insecure HTTP headers on the target URL."""
    insecure_headers = []
    response = requests.head(url, verify=False)
    headers = response.headers
    if 'server' in headers:
        insecure_headers.append(f"Insecure Server Header: {headers['server']}")
    if 'x-powered-by' in headers:
        insecure_headers.append(f"Insecure X-Powered-By Header: {headers['x-powered-by']}")
    return insecure_headers

if __name__ == "__main__":
    # Target host and ports to scan
    target_host = '127.0.0.1'
    target_ports = [21, 22, 80, 443]

    # Target URL for HTTP headers check
    target_url = 'http://example.com'

    # Check for open ports
    open_ports = check_open_ports(target_host, target_ports)
    if open_ports:
        print(f"Open ports on {target_host}: {open_ports}")
    else:
        print(f"No open ports found on {target_host}")

    # Check for insecure HTTP headers
    insecure_headers = check_http_headers(target_url)
    if insecure_headers:
        print(f"Insecure HTTP headers on {target_url}:")
        for header in insecure_headers:
            print(header)
    else:
        print(f"No insecure HTTP headers found on {target_url}")
