from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature, encode_dss_signature

# Challenge from the server
challenge = "52f5466d03281f93"

# Signature components (R, S) from the client
response = "81ddb908b943f5b48d6c012f46a50a1e2e0d7755,891e7587770b9c9c0e706163701d875e8800e17b"

# Elliptic Curve Parameters (Example: secp256r1)
curve = ec.SECP256R1()
# Function to verify the signature
def verify_signature(challenge, response, public_key):
    r, s = decode_response(response)

    # Convert the challenge to bytes
    challenge_bytes = bytes.fromhex(challenge)

    # Prepare the signature for verification
    signature_bytes = encode_dss_signature(r, s)

    # Create an ECDSA verifier
    verifier = ec.EllipticCurvePublicKey.from_encoded_point(curve, bytes.fromhex(public_key)).verifier(
        signature_bytes, ec.ECDSA(hashes.SHA256())
    )

    # Verify the signature
    try:
        verifier.update(challenge_bytes)
        verifier.verify()
        return True
    except Exception:
        return False
    
# Function to decode R, S values from the response
def decode_response(response):
    r_str, s_str = response.split(',')
    r = int(r_str, 16)
    s = int(s_str, 16)
    return r, s

# Function to verify the signature

# User's public key (Example with non-hex characters)
user_public_key = "DREAMQ1RGLSOLcuVTRVARRVrRrvw41ttIf42d"




# Verify the signature
is_valid_signature = verify_signature(challenge, response, user_public_key)

if is_valid_signature:
    print("Signature is valid!")
    # Proceed with extracting the flag
    # flag = ...
else:
    print("Signature is not valid.")
