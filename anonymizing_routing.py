import requests

def send_request_anonymously(url):
    """Send an HTTP request anonymously using Tor."""
    try:
        # Set Tor proxy
        proxies = {
            'http': 'socks5h://localhost:9050',
            'https': 'socks5h://localhost:9050'
        }
        
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            print(f"Response from {url}: {response.text}")
        else:
            print(f"Failed to get response from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":
    url = "http://example.com"  # Replace with the URL you want to access anonymously
    send_request_anonymously(url)
