class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.sender}{self.receiver}{self.amount}{self.timestamp}".encode()).hexdigest()

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
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
