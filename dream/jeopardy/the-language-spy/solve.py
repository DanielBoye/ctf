import json

def extract_text_from_log(log_data):
    text = ""
    for entry in log_data:
        if "params" in entry and "contentChanges" in entry["params"]:
            content_changes = entry["params"]["contentChanges"]
            for change in content_changes:
                if "text" in change:
                    text += change["text"]
    return text

def main():
    with open("server_logs.json", "r") as file:
        log_data = json.load(file)
    
    extracted_text = extract_text_from_log(log_data)
    print(extracted_text)

if __name__ == "__main__":
    main()

