def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = mod_inverse(e, phi)

    return n, e, d

def encrypt(message, n, e):
    encrypted = pow(message, e, n)
    return encrypted

def main():
    p = 61 
    q = 53 
    n, e, d = generate_keypair(p, q)

    message = 2089347503248975032984503248952394807230498234058
    ciphertext = encrypt(message, n, e)

    print(f"n = {n}")
    print(f"e = {e}")
    print(f"c = {ciphertext}") 
    print(f"p = {p}")
    print(f"q = {q}")

if __name__ == "__main__":
    main()
