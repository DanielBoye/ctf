from pwn import *

proc = remote('10.20.17.6', 5000)
proc.recvuntil(b"ad\x0a[3] Exit\x0a> ")
proc.write(b"2\x0a")
proc.recvuntil(b"\x0aThread ID: ")
proc.write(b"3lgIFWNuRiTHTmcv\x0a")
proc.recvuntil(b"Message: ")
proc.write(b"F\xa7\xf7\xa4\x11\xa1%!|_ \x0c\xb14\xd8\x08\x0a")
proc.recvuntil(b"9c709\x0aSignature: ")
proc.write(b"9d799c4be347e6f33cf7f31706d92db7d1f806cf0b472250f4e6985208c80d92879abc54628c2377a5a51383b534011cd7f4700e651508b2ab94e72f40f149146d9d2e814c3c737318e5dbc82ee049ac04ec8bafa210eb4c909dddcce8826c50a708810c5f92f2bce722adebea0c2a5b80c3c0f529425fade07db38f63b9c709\x0a")
proc.recvuntil(b"Attachment 0: ")
proc.write(b"\x0a")
proc.recvuntil(b"annot read input\x0a")
