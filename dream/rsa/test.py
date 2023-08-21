from Crypto.PublicKey import RSA
import base64

def rsa_decrypt(ciphertext, n, e, p, q):
    p, q, n, e = int(p), int(q), int(n), int(e)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    key = RSA.construct((n, e, d, p, q))
    encrypted_data = base64.b64decode(ciphertext)
    decrypted_data = key.decrypt(encrypted_data)
    return decrypted_data.decode()

if __name__ == "__main__":
    n = input("Enter the value of n: ")
    e = input("Enter the value of e: ")
    c = input("Enter the ciphertext to decrypt: ")
    p = input("Enter the value of p: ")
    q = input("Enter the value of q: ")

    decrypted_message = rsa_decrypt(c, n, e, p, q)
    print("Decrypted message:", decrypted_message)
