import requests
from stem import Signal
from stem.control import Controller

# Initialize Tor controller
def init_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_tor_password")
        return controller

# Get a new Tor IP address
def renew_tor_ip(controller):
    controller.signal(Signal.NEWNYM)

# Send an anonymous HTTP request using Tor
def send_anonymous_request(url):
    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
    try:
        response = session.get(url)
        if response.status_code == 200:
            print(f"Response from {url}: {response.text}")
        else:
            print(f"Failed to get response from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":
    # Initialize Tor controller
    controller = init_tor()

    # Renew Tor IP address
    renew_tor_ip(controller)

    # Send anonymous request
    url = "http://example.com"  # Replace with the URL you want to access anonymously
    send_anonymous_request(url)
