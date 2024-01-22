import random

flag_string = "flag{8yt3_c0d3_s0_c00l}"
flag = list(flag_string)

original_flag_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

swaped_flag_list = [
    11,
    6,
    10,
    18,
    8,
    17,
    5,
    15,
    0,
    14,
    19,
    22,
    16,
    1,
    3,
    13,
    4,
    2,
    7,
    20,
    21,
    9
]

# 1. Push "random" values
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

pushed = push1(flag)
print(pushed)

# Complete bytecode
# print("Complete")
# print(push1_with_60(flag))

for i in range(0, 22):
    print(original_flag_list[i], swaped_flag_list[i])
    
print(original_flag_list)
print(swaped_flag_list)


# 2. Swap values to the flag original state
def swap_values(pushed):
    swap = pushed.strip('0x')




    return swap

print("Swap values back to original state")
print(swap_values(pushed))