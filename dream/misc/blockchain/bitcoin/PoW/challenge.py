import random
import hashlib
import time
from flask import Flask, request, jsonify, session, redirect

with open("flag.txt", "r") as flag_file:
    flag = flag_file.read().strip()

flag_parts = [flag[i:i+1] for i in range(0, len(flag), 1)]
current_flag_index = 0

difficulty = 5
block_generation_time = 1 
mined_blocks = 0
prev_block_hash = hashlib.sha256(str(random.randint(0, 1000)).encode()).hexdigest()
required_blocks = len(flag)

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions

    def build_merkle_root(self):
        if len(self.transactions) == 0:
            return None
        elif len(self.transactions) == 1:
            return hashlib.sha256(self.transactions[0].encode()).hexdigest()

        # List to store intermediate merkle tree layers
        layers = [self.transactions]

        while len(layers[-1]) > 1:
            new_layer = []

            # Pair adjacent transactions and hash them together
            for i in range(0, len(layers[-1]), 2):
                left_tx = layers[-1][i]
                right_tx = layers[-1][i + 1] if i + 1 < len(layers[-1]) else left_tx
                combined_hash = hashlib.sha256((left_tx + right_tx).encode()).hexdigest()
                new_layer.append(combined_hash)

            layers.append(new_layer)

        return layers[-1][0]

def adjust_difficulty(difficulty, time_taken):
    target_time = block_generation_time
    if time_taken < target_time:
        return difficulty + 0.1
    elif time_taken > target_time:
        return max(difficulty - 0.1, 0.1)
    return difficulty


def proof_of_work(block_data, difficulty):
    nonce = 0
    prefix = "0" * int(difficulty)
    while True:
        block = str(nonce) + block_data
        hash_result = hashlib.sha256(block.encode()).hexdigest()

        if hash_result.startswith(prefix):
            return nonce
        nonce += 1


def generate_random_string(length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(charset) for _ in range(length))

app = Flask(__name__)
app.secret_key = "your_secret_key"

def build_merkle_root(transactions):
    merkle_tree = MerkleTree(transactions)
    merkle_root = merkle_tree.build_merkle_root()
    return merkle_root

@app.route('/', methods=['GET'])
def get_block_info():
    global current_flag_index

    transactions = [
        "TX123",
        "TX456",
        "TX789",
    ]
    merkle_root = build_merkle_root(transactions)

    # Display block information
    block_height = 1
    block_data = merkle_root + prev_block_hash
    timestamp = time.time()
    random_tx = generate_random_string(10)
    block = str(0) + block_data + str(timestamp) + random_tx
    hash_result = hashlib.sha256(block.encode()).hexdigest()

    block_info = {
        "Block Height": block_height,
        "Previous Block Hash": prev_block_hash,
        "Merkle Root": merkle_root,
        "Block Data": block_data,
        "Timestamp": timestamp,
        "Random Transaction": random_tx,
        "Block": block,
        "Block Hash": hash_result,
        "Required Blocks": required_blocks,
        "Flag Part": flag_parts[current_flag_index],
    }

    # Save the block_info in the session
    session['block_info'] = block_info

    return jsonify(block_info)

@app.route('/prev_hash', methods=['GET'])
def get_prev_block_hash():
    return prev_block_hash

@app.route('/submit_merkle_root', methods=['POST'])
def submit_merkle_root():
    global difficulty
    global prev_block_hash
    global mined_blocks
    global current_flag_index

    # Get block_info from the session
    block_info = session.get('block_info')

    data = request.form
    merkle_root = data['merkle_root']
    timestamp = time.time()

    # Participants need to include a random transaction in the block data
    random_tx = generate_random_string(10)
    block_data = merkle_root + prev_block_hash + str(timestamp) + random_tx

    # Perform Proof of Work and Mine the Block
    nonce = proof_of_work(block_data, difficulty)

    # Calculate the block reward using the current mined_blocks count
    block_reward = flag_parts[mined_blocks]

    # Add block reward to the block data
    block_data += f"REWARD{block_reward}"

    block = str(nonce) + block_data
    hash_result = hashlib.sha256(block.encode()).hexdigest()

    # Difficulty adjustment based on mining time
    new_timestamp = time.time()
    time_taken = new_timestamp - timestamp
    adjusted_difficulty = adjust_difficulty(difficulty, time_taken)

    # Update the difficulty for the next block
    difficulty = adjusted_difficulty

    # Update the previous block hash for the next block
    prev_block_hash = hashlib.sha256(hash_result.encode()).hexdigest()

    # Increment the mined_blocks count
    mined_blocks += 1

    # Check if the required_blocks limit has been reached
    if mined_blocks >= required_blocks:
        reset_blockchain()
    else:
        # Save the updated block_info in the session for the next iteration
        session['block_info'] = block_info
    return flag

@app.route('/reset', methods=['GET'])
def reset_blockchain():
    global current_flag_index
    global difficulty
    global prev_block_hash
    global mined_blocks

    session.clear()
    
    current_flag_index = 0
    difficulty = 1
    prev_block_hash = hashlib.sha256(str(random.randint(0, 1000)).encode()).hexdigest()
    mined_blocks = 0

    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
