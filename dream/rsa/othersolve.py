import hashlib

def decrypt_with_small_exponent(encrypted_flag, public_key, e, d):
    n, _ = public_key
    decrypted_flag = pow(encrypted_flag, d, n)
    return decrypted_flag

def brute_force_solve(encrypted_flag, e, n):
    for d in range(1, n):
        decrypted_flag = decrypt_with_small_exponent(encrypted_flag, (n, e), e, d)

        flag_hash = hex(decrypted_flag)[2:] 
        original_flag = bytes.fromhex(flag_hash).decode()
        
        if original_flag.startswith("ECSC2023"):
            return original_flag

def main():
    print("Welcome to the RSA race mf solver!")
    print("Your goal is to find the original flag.")

    encrypted_flag = 55714617865807800556648845825099941682542559715637518895746838894452327209112533422262498489978976922581431653309701709509732153593478482044955027153365078635824704335559211743385801883974458023166164761266348372443441036430056408
    e = 3 
    n = 18456944073709551617

    original_flag = brute_force_solve(encrypted_flag, e, n)

    if original_flag:
        print("Congratulations! The original flag is:", original_flag)
    else:
        print("Failed to find the original flag. Try increasing the range for d.")

if __name__ == "__main__":
    main()
