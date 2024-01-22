import random

flag_string = "flag{8yt3_c0d3_s0_c00l}"
flag = list(flag_string)

# 1. Push "random" vaules
def push1_with_60(flag):
    bytecode = "0x"
    bytecode += "60" + hex(ord(flag[11]))[2:]
    bytecode += "60" + hex(ord(flag[6]))[2:]
    bytecode += "60" + hex(ord(flag[10]))[2:]
    bytecode += "60" + hex(ord(flag[18]))[2:]
    bytecode += "60" + hex(ord(flag[8]))[2:]
    bytecode += "60" + hex(ord(flag[17]))[2:]
    bytecode += "60" + hex(ord(flag[5]))[2:]
    bytecode += "60" + hex(ord(flag[15]))[2:]
    bytecode += "60" + hex(ord(flag[0]))[2:]
    bytecode += "60" + hex(ord(flag[14]))[2:]
    bytecode += "60" + hex(ord(flag[19]))[2:]
    bytecode += "60" + hex(ord(flag[22]))[2:]
    bytecode += "60" + hex(ord(flag[16]))[2:]
    bytecode += "60" + hex(ord(flag[1]))[2:]
    bytecode += "60" + hex(ord(flag[3]))[2:]
    bytecode += "60" + hex(ord(flag[13]))[2:]
    bytecode += "60" + hex(ord(flag[4]))[2:]
    bytecode += "60" + hex(ord(flag[2]))[2:]
    bytecode += "60" + hex(ord(flag[7]))[2:]
    bytecode += "60" + hex(ord(flag[20]))[2:]
    bytecode += "60" + hex(ord(flag[21]))[2:]
    bytecode += "60" + hex(ord(flag[9]))[2:]

    return bytecode

def push1(flag):
    bytecode = "0x"
    bytecode += hex(ord(flag[11]))[2:]
    bytecode += hex(ord(flag[6]))[2:]
    bytecode += hex(ord(flag[10]))[2:]
    bytecode += hex(ord(flag[18]))[2:]
    bytecode += hex(ord(flag[8]))[2:]
    bytecode += hex(ord(flag[17]))[2:]
    bytecode += hex(ord(flag[5]))[2:]
    bytecode += hex(ord(flag[15]))[2:]
    bytecode += hex(ord(flag[0]))[2:]
    bytecode += hex(ord(flag[14]))[2:]
    bytecode += hex(ord(flag[19]))[2:]
    bytecode += hex(ord(flag[22]))[2:]
    bytecode += hex(ord(flag[16]))[2:]
    bytecode += hex(ord(flag[1]))[2:]
    bytecode += hex(ord(flag[3]))[2:]
    bytecode += hex(ord(flag[13]))[2:]
    bytecode += hex(ord(flag[4]))[2:]
    bytecode += hex(ord(flag[2]))[2:]
    bytecode += hex(ord(flag[7]))[2:]
    bytecode += hex(ord(flag[20]))[2:]
    bytecode += hex(ord(flag[21]))[2:]
    bytecode += hex(ord(flag[9]))[2:]

    return bytecode

print("Pushed values")
print(push1(flag))

print("Complete")
print(push1_with_60(flag))


# 2. Swap values to the flag original state

# 3. Push "yeah :sunglasses:" onto the stack (in like a byte or sum)

# 4. Swap values to the original swap state

# 5. Return the hash of this swap value