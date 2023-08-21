import json

with open('server_logs.json', 'r') as file:
    log_entries = json.load(file)

text_sentence = ""
for entry in log_entries:
    uri = entry["params"]["textDocument"]["uri"]
    if uri == "file:///home/work/no_secrets_here.txt":
        text = entry["params"]["contentChanges"][0]["text"]
        text_sentence += text

print("Text Sentence:", text_sentence)
