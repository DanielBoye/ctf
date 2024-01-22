def implode(input, antall):
    størrelse = len(input) // antall
    fragmenter = []
    
    for i in range(0, len(input), størrelse):
        fragment = input[i:i+størrelse]
        fragmenter.append(fragment)
    
    return fragmenter

def reverse_explode(input, otp):
    eksplosjon = [''.join([chr(ord(c) - 2) for c in fragment]) for fragment in input]
    # slede = ''.join(eksplosjon[i] for i in reversed(otp))
    return eksplosjon

with open("pinneved.txt", "r") as file:
    pinneved = file.read()

# Assuming the same OTP is used for reversal
reversed_slede = implode(pinneved, 24)
reversed_text = reverse_explode(reversed_slede, [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15])

print(reversed_text)

with open("test.txt", "w") as file:
    file.write(''.join(reversed_text))