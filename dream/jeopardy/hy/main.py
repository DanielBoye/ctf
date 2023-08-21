#!/usr/bin/env python3
from itertools import product

def build_dict(a1, a2, a3, *rest):
    thisitem = {chr(a1): a2 ^ a3}
    if len(rest):
        thisitem.update(build_dict(*rest))
    return thisitem

def get_byte(flag, n):
    index = n * 2
    if index < len(flag):
        return int(flag[index:index+2], 16)
    return ""

def get_salt(flag):
    return [get_byte(flag, index) for index in range(2, len(flag) // 2, 3)]

def validate_salt(flag):
    return all(x > 200 for x in get_salt(flag))

def get_multiplier(n):
    return int(n) if n in "23456789" else 1

def flag_to_dict(flag):
    return build_dict(*[get_byte(flag, index) for index in range(0, len(flag) // 2)])

def dict_to_words(flag_dict):
    return "".join(flag_dict.keys()) + "_" + "".join(chr(x) for x in flag_dict.values())

def compute_target_product(flag):
    salt = get_salt(flag)
    multipliers = [get_multiplier(char) for char in flag]
    product = 1
    for num in salt + multipliers:
        product *= num
    return product

def validate_flag(flag, target_product, target_string):
    if not validate_salt(flag):
        return False
    computed_target_product = compute_target_product(flag)
    if target_product != computed_target_product:
        return False
    if target_string != dict_to_words(flag_to_dict(flag)):
        return False
    return True

def generate_flag(flag_chars, target_product, target_string):
    flag_length = len(target_string)

    for flag_candidate in product(flag_chars, repeat=flag_length):
        flag = "".join(flag_candidate)
        if validate_flag(flag, target_product, target_string):
            print(f"CTF{{{flag}}} is correct!")
            return flag

def main():
    try:
        # Test:
        validate_flag("6c98f46fb1d876a3d06583f3", 60134327409746903040, "love_lisp")
        print("Test passed")

    except AssertionError:
        print("Test failed")

    # Challenge:
    target_product = 1342723557762272448000
    target_string = "easy_flag"
    flag_chars = "0123456789abcdef"
    flag = generate_flag(flag_chars, target_product, target_string)

if __name__ == "__main__":
    main()
