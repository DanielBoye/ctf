import hashlib
import random
import string
import time
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transaction_id = hashlib.sha256((sender + receiver + str(amount) + str(time.time())).encode()).hexdigest()

class Block:
    def __init__(self, previous_hash):
        self.previous_hash = previous_hash
        self.transactions = []
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.previous_hash}{self.transactions}{self.nonce}".encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3 

    def create_genesis_block(self):
        return Block("0")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.get_last_block().transactions.append(transaction)

    def mine(self):
        new_block = Block(self.get_last_block().hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def generate_weak_private_key():
    # This is a simplified method to generate weak private keys for demonstration purposes.
    # In a real-world scenario, a more secure method should be used.
    return random.randint(1, 1000)

# Create the Flask application
app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"  # Change this to a secure secret key

blockchain = Blockchain()

# User's public-private key pairs and private keys
users = {
    "Alice": {"public_key": hashlib.sha256(str(generate_weak_private_key()).encode()).hexdigest(), "private_key": generate_weak_private_key()},
    "Bob": {"public_key": hashlib.sha256(str(generate_weak_private_key()).encode()).hexdigest(), "private_key": generate_weak_private_key()},
}

# Hidden flag inside the wallet
with open("flag.txt", "r") as flag_file:
    flag = flag_file.read().strip()

# Fake transactions for the dashboard
fake_transactions = [
    Transaction("Alice", "Bob", 10),
    Transaction("Bob", "Charlie", 5),
    Transaction("Alice", "Charlie", 3),
    Transaction("Charlie", "Alice", 2),
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        public_key = request.form.get("public_key")
        private_key = int(request.form.get("private_key"))

        for username, user_data in users.items():
            if user_data["public_key"] == public_key and user_data["private_key"] == private_key:
                session["logged_in"] = True
                session["public_key"] = public_key
                session["private_key"] = private_key
                return redirect(url_for("dashboard"))

        return render_template("index.html", message="Invalid credentials. Please try again.", users=users)

    return render_template("index.html", users=users)

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("index"))

    public_key = session.get("public_key")
    private_key = session.get("private_key")
    username = next((username for username, user_data in users.items() if user_data["public_key"] == public_key), "")

    user_transactions = [tx for tx in fake_transactions if tx.sender == username or tx.receiver == username]

    # Get the latest transactions for display
    latest_transactions = fake_transactions[-5:]

    return render_template("dashboard.html", username=username, transactions=user_transactions, flag=flag, latest_transactions=latest_transactions)

@app.route("/public_keys", methods=["GET"])
def public_keys():
    # Include the public keys in the response
    public_keys_only = {user: user_data["public_key"] for user, user_data in users.items()}
    return jsonify(public_keys_only)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("public_key", None)
    session.pop("private_key", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
