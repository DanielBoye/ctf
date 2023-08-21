from pwn import *

def calculate_offset():
    rip_value = 0x40187c

    pattern = cyclic(100)

    offset = cyclic_find(p32(rip_value))

    print("Offset:", offset)

if __name__ == "__main__":
    calculate_offset()
