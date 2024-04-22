import hashlib
import json

class SecureMessagingApp:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, recipient, message, encryption_key):
        """Send a secure message."""
        encrypted_message = self.encrypt_message(message, encryption_key)
        message_data = {
            'sender': sender,
            'recipient': recipient,
            'encrypted_message': encrypted_message
        }
        self.messages.append(message_data)

    def receive_message(self, recipient, decryption_key):
        """Receive and decrypt messages for a recipient."""
        received_messages = []
        for message in self.messages:
            if message['recipient'] == recipient:
                decrypted_message = self.decrypt_message(message['encrypted_message'], decryption_key)
                received_message = {
                    'sender': message['sender'],
                    'message': decrypted_message
                }
                received_messages.append(received_message)
        return received_messages

    def encrypt_message(self, message, key):
        """Encrypt a message using a key."""
        # Simplified encryption using SHA256 hash
        encrypted_message = hashlib.sha256((message + key).encode()).hexdigest()
        return encrypted_message

    def decrypt_message(self, encrypted_message, key):
        """Decrypt a message using a key."""
        # Simplified decryption using SHA256 hash
        decrypted_message = hashlib.sha256(encrypted_message.encode()).hexdigest()
        return decrypted_message

if __name__ == "__main__":
    app = SecureMessagingApp()

    # Generate encryption and decryption keys (simplified example)
    encryption_key = "encryption_key"
    decryption_key = "decryption_key"

    # Send a message
    sender = "Alice"
    recipient = "Bob"
    message = "Hello, Bob!"
    app.send_message(sender, recipient, message, encryption_key)

    # Receive messages
    received_messages = app.receive_message(recipient, decryption_key)
    for received_message in received_messages:
        print(f"Received message from {received_message['sender']}: {received_message['message']}")
