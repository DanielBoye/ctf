from Crypto.Util.number import long_to_bytes

n = 3233
e = 17
c = 64
p = 61
q = 53

# Calculate φ(n)
phi_n = (p - 1) * (q - 1)

# Calculate the private exponent 'd'
d = pow(e, -1, phi_n)

# Decrypt the message
m = pow(c, d, n)
print(m)
# Convert the decrypted message from integer to bytes
plaintext = long_to_bytes(m)

print("Decrypted message:", plaintext)
