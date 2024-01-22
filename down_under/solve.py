from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/56897e79a3a94d71ab53b5b1b187bfbe')  )

signature = '0xd6d2b369'

function_name = w3.to_hex(w3.keccak(text=signature)[:4])
print(function_name)
