import requests
import os
import secrets

# Replace the following URL with the URL of the server running the challenge.
BASE_URL = "http://litctf.org:31780"

def upload_file(filename):
    files = {"file": open(filename, "rb")}
    response = requests.post(BASE_URL + "/upload", files=files)
    submission_id = response.text.split("Your submission id is: ")[1].strip(" .")
    return submission_id

def judge_submission(submission_id):
    data = {"id": submission_id}
    response = requests.post(BASE_URL + "/judge", data=data)
    return response.text.strip()

def check_status(submission_id):
    response = requests.get(BASE_URL + "/status/" + submission_id)
    return response.text.strip()

# Step 1: Create a file with the winning content.
winning_file_content = "winner!!"
winning_file = "winning_art.txt"
with open(winning_file, "w") as f:
    f.write(winning_file_content)

# Step 2: Upload the file containing the "winner!!" string.
submission_id = upload_file(winning_file)
print("Submission ID:", submission_id)

# Step 3: Trigger the judging process.
judge_submission(submission_id)

# Step 4: Check the status to see if we won.
status_response = check_status(submission_id)
print(status_response)

# Clean up the files (optional).
os.remove(winning_file)
