import hashlib
from multiprocessing import Pool

def hash_password(password):
    """Hash the password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, hash_to_check):
    """Check if the password matches the given hash."""
    hashed_password = hash_password(password)
    if hashed_password == hash_to_check:
        return password
    return None

def password_cracker(passwords, hash_to_check, num_processes):
    """Crack the password using multiple processes."""
    pool = Pool(processes=num_processes)
    results = pool.starmap(check_password, [(password, hash_to_check) for password in passwords])
    pool.close()
    pool.join()

    for result in results:
        if result:
            print(f"Password cracked: {result}")
            break
    else:
        print("Password not found")

if __name__ == "__main__":
    passwords = ["password1", "password2", "password3"]  # Replace with the list of passwords to check
    hash_to_check = "your_hashed_password"  # Replace with the hash to check
    num_processes = 4  # Number of processes to use for parallel processing

    password_cracker(passwords, hash_to_check, num_processes)
