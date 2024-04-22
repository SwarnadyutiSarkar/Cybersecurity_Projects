from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_key_pair():
    """Generate RSA key pair."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign_message(private_key, message):
    """Sign a message using the private key."""
    key = RSA.import_key(private_key)
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_signature(public_key, message, signature):
    """Verify a signature using the public key."""
    key = RSA.import_key(public_key)
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    private_key, public_key = generate_key_pair()

    message = "Hello, World!"
    signature = sign_message(private_key, message)
    print(f"Signature: {signature.hex()}")

    is_valid = verify_signature(public_key, message, signature)
    print(f"Signature is valid: {is_valid}")
