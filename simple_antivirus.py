import hashlib

def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_file(file_path, signatures):
    """Scan a file for malicious signatures."""
    file_hash = calculate_hash(file_path)
    if file_hash in signatures:
        return True, f"Malicious signature detected for file: {file_path}"
    else:
        return False, f"File is clean: {file_path}"

if __name__ == "__main__":
    # Define malicious file signatures (Replace with actual malicious file hashes)
    signatures = {
        'malicious_hash_1',
        'malicious_hash_2',
        'malicious_hash_3',
    }

    # File to scan
    file_path = 'sample_malicious_file.exe'

    # Scan the file
    is_infected, message = scan_file(file_path, signatures)

    # Print scan result
    if is_infected:
        print(f"Infected: {message}")
    else:
        print(f"Clean: {message}")
