import hashlib
import itertools

def generate_possible_flags(alphabet, length):
    return [''.join(combination) for combination in itertools.product(alphabet, repeat=length)]

def brute_force_solve(encrypted_flag, alphabet, max_length):
    for length in range(1, max_length + 1):
        possible_flags = generate_possible_flags(alphabet, length)
        for flag in possible_flags:
            if hashlib.sha256(flag.encode()).hexdigest() == encrypted_flag:
                return flag
    return None

def main():
    print("Welcome to the Crypto Conundrum Challenge Solver!")

    # Provide the encrypted flag to solve
    encrypted_flag = input("Enter the SHA-256 hash of the encrypted flag: ").strip()

    # Provide the alphabet used for generating the flag
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!?#.:*-"

    # Provide the maximum length of the flag to be brute forced
    max_length = 5

    # Attempt to solve the challenge using brute force
    solution = brute_force_solve(encrypted_flag, alphabet, max_length)

    if solution:
        print("Congratulations! The flag is:", solution)
    else:
        print("Couldn't find the flag. Try increasing the maximum length or checking the alphabet used.")

if __name__ == "__main__":
    main()
