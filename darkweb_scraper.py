import requests
from bs4 import BeautifulSoup

def darkweb_scraper(url):
    """Scrape content from a dark web URL."""
    try:
        # Send HTTP request
        response = requests.get(url)
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract relevant information
            content = soup.get_text()
            print(content)
        else:
            print(f"Failed to scrape URL {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error scraping URL: {e}")

if __name__ == "__main__":
    url = "http://darkwebwebsite.onion"  # Replace with the dark web URL you want to scrape
    darkweb_scraper(url)
