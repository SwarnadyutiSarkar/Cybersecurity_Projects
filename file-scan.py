import hashlib
import requests

# List of known malicious file hashes (for demo purposes, these are random)
known_malicious_hashes = {
    'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',  # Example hash
    'b10a8db164e0754105b7a99be72e3fe5fbee74b891f4e7c6dc7e5b4f9ebf4e35',  # Example hash
}

def download_file(url, local_filename):
    """Download a file from a URL."""
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def calculate_file_hash(filename, hash_function='sha256'):
    """Calculate the hash of a file."""
    h = hashlib.new(hash_function)
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def scan_file(filename):
    """Scan the file for known malware."""
    file_hash = calculate_file_hash(filename)
    if file_hash in known_malicious_hashes:
        print(f"Alert! The file '{filename}' is flagged as malicious.")
    else:
        print(f"The file '{filename}' is clean.")

def main():
    # URL of the file to be downloaded (for demo purposes, replace with a real URL)
    file_url = 'https://example.com/somefile.txt'
    local_filename = 'downloaded_file.txt'

    # Step 1: Download the file
    download_file(file_url, local_filename)
    print(f"File downloaded as '{local_filename}'")

    # Step 2: Scan the downloaded file
    scan_file(local_filename)

if __name__ == "__main__":
    main()
