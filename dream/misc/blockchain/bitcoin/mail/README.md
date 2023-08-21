# PoW

## Daniel Boye

## Category: {Blockchain, Misc}

## Problem Statement

The script is a server implementation of a blockchain-based PoW. Participants can interact with the server to mine blocks and reveal characters of the hidden flag when all of the blocks are mined. The blockchain is designed to adjust its difficulty dynamically based on mining time, making it more challenging to mine subsequent blocks.

Participants use Proof of Work (PoW) to mine blocks, requiring them to find a valid nonce that produces a hash with a specific number of leading zeros. The difficulty increases if a block is mined too quickly and decreases if it takes too long, ensuring a consistent block generation time.

Once a block is mined, the server logs that and when they have mined as many blocks as the length of the flag. Participants uncover the flag. They can reset the blockchain to start over and attempt to mine the flag again.

The script showcases participants' abilities to implement own custom cryptographic mining algorithms and manage block difficulty while mining to uncover the flag's hidden message while learning about features such as merkle trees and roots. 

## Flavor Text

just finished up creating my first custom PoW blockchain! please don't look at the code though, i suck at programming.

proud of myself though. i implemented block generation and mining, merkle trees and a difficulty adjustment. such cool words huh

btw a block contains a merkle root, a previous block hash, a timestamp, and a random transaction. just though i would let you know

and with the merkle tree. i wrote it so we use it to build the merkle root from a list of transactions. it is included in the block data, making it a part of the PoW process.

oh well, merkle her and merkel there. not so important...

it sounds cool and all but a lot of the code could be written better, but hey it works for now. just try it yourself!

i have also created a motto for this project, "the more you mine, the higher the reward is!"

## Difficulty

- **Medium:** 

## Challenge Information (2/3)

- **Estimated Solve Time:** 20min-60min
- **Solver Script:** 

```python
import requests
import hashlib
import time

url = 'http://localhost:5000/'
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
    global flag_parts  # Define as global here

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
```

## Type

- **One Docker Container** See zip file attatched in the email. It is the handout with a fake flag inside of it. For setting it up, I would advise you too choose the flag.txt I have provided, or something else that you would prefer. 
