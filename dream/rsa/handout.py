import random
import hashlib
from Crypto.PublicKey import RSA

def generate_keypair(bits=1024, e=3):
    key = RSA.generate(bits, e=e)
    public_key = (key.n, key.e)
    private_key = (key.n, key.d)
    return public_key, private_key

def encrypt(plain_text, public_key):
    n, e = public_key
    encrypted_flag = pow(plain_text, e, n)
    return encrypted_flag

def main():
    print("Welcome to the Weak Crypto Conundrum Challenge!")
    print("Your goal is to find the encrypted flag.")

    key_size = 1024  # Minimum allowed key size
    public_exponent = 3  # A small public exponent for making it easy
    public_key, private_key = generate_keypair(bits=key_size, e=public_exponent)

    flag = "ECSC2023{weak_rsa_flag}"
    flag_hash = hashlib.sha256(flag.encode()).hexdigest()
    encrypted_flag = encrypt(int(flag_hash, 16), public_key)

    print("Challenge: Find the encrypted flag (decimal representation):")
    print(encrypted_flag)

    while True:
        user_input = input("Enter your guess for the encrypted flag: ").strip()
        if int(user_input) == encrypted_flag:
            print("Congratulations! You found the encrypted flag!")
            break
        else:
            print("Oops! That's not the correct encrypted flag. Try again!")

if __name__ == "__main__":
    main()
