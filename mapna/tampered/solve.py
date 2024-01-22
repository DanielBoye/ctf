import re

def validate_flag(flag):
    pattern = r'MAPNA{[0-9a-zA-Z_-]+.!?|}'
    return re.fullmatch(pattern, flag) is not None

def main():
    file_path = 'flags.txt'

    try:
        with open(file_path, 'r') as file:
            flags = file.read().splitlines()
        
        for flag in flags:
            if validate_flag(flag):
                print(f"Valid Flag: {flag}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    main()
