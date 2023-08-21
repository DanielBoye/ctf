import hashlib
import requests

def find_collision():
    target_hash = "b6589fc6ab0dc82cf12099d1c2d40ab994e8410c"
    counter = 0

    while True:
        candidate = str(counter)
        candidate_hash = hashlib.sha1(candidate.encode()).hexdigest()

        if candidate_hash == target_hash:
            return candidate

        counter += 1

def solve_ctf_challenge(base_url):
    collision_string = find_collision()
    username = "admin"
    password = collision_string

    params = {
        "txt_uname": username,
        "txt_pwd": password,
        "but_submit": "Submit"
    }

    response = requests.get(base_url, params=params)
    
    print(response)

if __name__ == "__main__":
    base_url = "https://ch301497130979.ch.eng.run"
    solve_ctf_challenge(base_url)
