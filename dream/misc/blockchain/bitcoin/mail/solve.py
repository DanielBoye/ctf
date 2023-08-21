import requests
import hashlib
import time

# Point this to the docker container
url = 'http://pow.ex.sec-aau.dk:5000/'
flag_parts = []

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def mine_block(block_data, difficulty):
    prefix = "0" * difficulty
    nonce = 0
    while True:
        block = str(nonce) + block_data
        block_hash = calculate_hash(block)
        if block_hash.startswith(prefix):
            return block, nonce, block_hash
        nonce += 1

def get_block_info():
    response = requests.get(url)
    block_info = response.json()
    return block_info

def submit_merkle_root(merkle_root):
    data = {'merkle_root': merkle_root}
    response = requests.post(url + 'submit_merkle_root', data=data)
    return response.text

def main():
    global flag_parts

    # Step 1: Get block information from the server
    block_info = get_block_info()

    # Step 2: Mine the blocks and obtain the flag
    difficulty = block_info['Block Height']
    block_number = 1

    while block_number <= block_info['Required Blocks']:
        # Mine the block
        block_data = block_info['Merkle Root'] + block_info['Previous Block Hash'] + str(block_info['Timestamp']) + block_info['Random Transaction']
        block, nonce, block_hash = mine_block(block_data, difficulty)

        print(f"Mining Block {block_number}")
        # Submit the mined block's merkle root to the server
        response = submit_merkle_root(merkle_root=block_info['Merkle Root'])
        
        if response:
            print("Success!")
        

        block_number += 1
    print(f"\n{response}")
if __name__ == '__main__':
    main()
