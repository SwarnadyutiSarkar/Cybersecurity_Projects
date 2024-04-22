import hashlib
import json

class SecureCryptocurrencyWallet:
    def __init__(self):
        self.transactions = []
        self.balance = 0

    def add_transaction(self, sender, recipient, amount, signature):
        """Add a new transaction to the wallet."""
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'signature': signature
        }
        self.transactions.append(transaction)

    def calculate_balance(self):
        """Calculate the wallet balance."""
        self.balance = 0
        for transaction in self.transactions:
            if transaction['sender'] == 'Genesis':
                self.balance -= transaction['amount']
            elif transaction['recipient'] == 'Genesis':
                self.balance += transaction['amount']

    def sign_transaction(self, sender, recipient, amount, private_key):
        """Sign a transaction using the private key."""
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        signature = hashlib.sha256(json.dumps(transaction).encode()).hexdigest()  # Simplified signing method
        return signature

if __name__ == "__main__":
    wallet = SecureCryptocurrencyWallet()

    # Generate keys (simplified example)
    private_key = "private_key"
    public_key = "public_key"

    # Create and sign a transaction
    sender = public_key
    recipient = "recipient_public_key"
    amount = 10
    signature = wallet.sign_transaction(sender, recipient, amount, private_key)
    wallet.add_transaction(sender, recipient, amount, signature)

    # Calculate balance
    wallet.calculate_balance()
    print(f"Wallet balance: {wallet.balance}")
