import random
import hashlib

def generate_flag():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!?#.:*-"
    flag = ''.join(random.choice(alphabet) for _ in range(5))
    return flag

def encrypt_flag(flag):
    # You can use any encryption algorithm of your choice here
    # For simplicity, we'll use SHA-256 as a basic encryption method
    encrypted_flag = hashlib.sha256(flag.encode()).hexdigest()
    return encrypted_flag

def main():
    print("Welcome to the Crypto Conundrum Challenge!")
    print("Your goal is to find the encrypted flag.")

    # Generate the flag
    flag = generate_flag()
    encrypted_flag = encrypt_flag(flag)

    print("Challenge: Find the encrypted flag that matches this SHA-256 hash:")
    print(encrypted_flag)

    # For testing purposes, you can uncomment the following line to see the original flag
    print("Original Flag:", flag)

    # Prompt the participant for their answer
    while True:
        user_input = input("Enter your guess for the flag: ").strip()
        if hashlib.sha256(user_input.encode()).hexdigest() == encrypted_flag:
            print("Congratulations! You found the flag!")
            break
        else:
            print("Oops! That's not the correct flag. Try again!")

if __name__ == "__main__":
    main()
