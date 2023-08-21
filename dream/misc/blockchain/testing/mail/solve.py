import requests
from bs4 import BeautifulSoup

# Change the port to the Flask app's running address. 
BASE_URL = "http://127.0.0.1:5002"
session = requests.Session()

def try_login(public_key, private_key):
    data = {
        "public_key": public_key,
        "private_key": private_key
    }
    response = session.post(f"{BASE_URL}/", data=data)
    return response

def get_flag_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    flag_element = soup.find("p", {"id": "flag"})
    if flag_element:
        flag = flag_element.text.strip().replace("Flag: ", "")
        return flag
    return None

def combine_flags(alice_flag, bob_flag):
    full_flag = alice_flag + bob_flag
    return full_flag

def main():
    global alice_flag_part
    global bob_flag_part

    public_keys_response = session.get(f"{BASE_URL}/public_keys")
    public_keys_data = public_keys_response.json()

    for username, user_data in public_keys_data.items():
        public_key = user_data
        print(f"\nTrying to log in as {username} with public key: {public_key}")

        for private_key_guess in range(1, 10001):
            response = try_login(public_key, private_key_guess)
            if "Welcome" in response.text:
                flag = get_flag_from_html(response.text)
                if flag:
                    print(f"\nFlag for {username}: {flag}")
                    print(f"Private key that worked: {private_key_guess}")
                    if username == "Alice":
                        alice_flag_part = flag
                    elif username == "Bob":
                        bob_flag_part = flag
                    if alice_flag_part and bob_flag_part:
                        full_flag = combine_flags(alice_flag_part, bob_flag_part)
                        print(f"\nFull flag: {full_flag}\n")
                        return
                else:
                    print(f"Flag not found for {username}")
                break

if __name__ == "__main__":
    alice_flag_part = ""
    bob_flag_part = ""
    main()
