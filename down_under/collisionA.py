import hashlib

# Target hash value you want to collide with
target_hash = "0xc6529caaeee374d860f327f47f18a6585df16f8d87581d71bccbe16af79e86e1"

def find_collision(target_hash, input1, input2):
    hash1 = hashlib.sha256(input1.encode()).hexdigest()
    hash2 = hashlib.sha256(input2.encode()).hexdigest()
    
    if hash1 == target_hash and hash2 == target_hash:
        print(f"Collision found!")
        print(f"Input1: {input1}")
        print(f"Input2: {input2}")
        return True
    print("", input1)
    return False

# Example usage: Find a collision for "input1" and "input2"
input1 = "a"  # Change this to test different values
input2 = "bc" # Change this to test different values

while not find_collision(target_hash, input1, input2):
    # Increment or manipulate input1 and input2
    input1 += "a"
    input2 = input2[1:]
