from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import base64

def rsa_encrypt(message, n, e):
    key = get_random_bytes(16)

    cipher_aes = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())

    rsa_key = RSA.construct((int(n), int(e)))
    cipher_rsa = PKCS1_OAEP.new(rsa_key)

    encrypted_key = cipher_rsa.encrypt(key)
    encoded_key = base64.b64encode(encrypted_key).decode()
    encoded_message = base64.b64encode(cipher_aes.nonce + ciphertext + tag).decode()
    return f"{encoded_key}|{encoded_message}"

if __name__ == "__main__":
    n = input("Enter the value of n: ")
    e = input("Enter the value of e: ")
    message = input("Enter the message to encrypt: ")

    encrypted_message = rsa_encrypt(message, n, e)
    print("Encrypted message:", encrypted_message)
