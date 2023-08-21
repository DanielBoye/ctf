import hashlib

def generate_public_key(private_key):
    return hashlib.sha256(str(private_key).encode()).hexdigest()

if __name__ == "__main__":
    num_keys = 10  # Set the number of public keys you want to generate
    for private_key in range(1, num_keys + 1):
        public_key = generate_public_key(private_key)
        print(f"Private Key: {private_key}, Public Key: {public_key}")
