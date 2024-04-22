import requests

def search_0day_vulnerabilities(product_name):
    """Search for 0-day vulnerabilities related to a product."""
    try:
        # Send HTTP request to vulnerability database (simplified example)
        url = f"https://vulndb.com/search?product={product_name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse and extract vulnerability information (simplified example)
            vulnerabilities = response.json()
            for vulnerability in vulnerabilities:
                print(f"Found 0-day vulnerability: {vulnerability}")
        else:
            print(f"Failed to search for 0-day vulnerabilities. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error searching for 0-day vulnerabilities: {e}")

if __name__ == "__main__":
    product_name = "example_product"  # Replace with the product name you want to search for
    search_0day_vulnerabilities(product_name)
