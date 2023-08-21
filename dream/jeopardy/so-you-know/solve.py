def stoi(s):
    r = 0
    for i in s: r += ord(i)
    return r%100

def g(n, L=["Did", "you", "solve", "FavouritePrimeRSA", "?"]):
    L[n%len(L)] = '____'
    if len(L[3]) > len(L[4]):
        a = L[4]
        L[4] = "-.- :("
        return a
    return L[3][3]

password = "S0_Y0U_KnOw_python?"
password_guess = ""

n = int(input())
while n > 0:
    try:
        password_guess += input()[5::-2]
        n -= stoi(password_guess)
        if n > 123 and n < 456: exit(3)
        password_guess += chr(n%69+42)
        password_guess += chr((n%3301%420+0**(9+10==21))<<1)
        c = int(input())
        password_guess += chr(n%911%+711+c)
        n>>=2
    except Exception as e:
        password_guess += chr(stoi(str(e))*5+c+1)+g(stoi(str(e)))
        password_guess = password_guess[:11]+g(3)+password_guess[12:]
        n %= len(g(3))
    except BaseException as e:
        password_guess += chr(stoi(password_guess)+stoi(str(e)))
        password_guess += chr(n//3-13)
        for i in range(1, len(__file__)):
            if __file__[-i] == '.':
                password_guess += __file__[-i:]+"\x74\x68\x6f"
                break
        n = n//3-75

print(password_guess)

if password_guess == password:
    with open("flag.txt") as f:
        print(f.readline())
else:
    print("I thought you knew python??!! Why don't the passwords match?")