from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/56897e79a3a94d71ab53b5b1b187bfbe')  )

# The Ethereum address you want to query
address = '0x24d1a591b816c175ebf4cd62277ecccda42d1211'

# Fetch all transactions associated with the address
transactions = w3.eth.getTransactionsByAddress(address)

for tx in transactions:
    # Get the transaction hash
    tx_hash = tx['hash'].hex()
    
    # Get the value sent in Wei
    value_wei = tx['value']
    
    # Convert Wei to Ether
    value_ether = w3.fromWei(value_wei, 'ether')
    
    print(f'Transaction Hash: {tx_hash}')
    print(f'Value (in Wei): {value_wei}')
    print(f'Value (in Ether): {value_ether} Ether')
    print('---')