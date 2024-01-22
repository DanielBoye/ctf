# Script to extract and print dialogue from subtitles file

subtitles_file_path = "/mnt/c/Users/danie/ctf/iris/not-just-media/subtitles"

def extract_dialogue(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        in_dialogue_section = False
        for line in file:
            line = line.strip()
            if line.startswith("Dialogue:"):
                in_dialogue_section = True
                # Extract the dialogue text and print it
                dialogue_text = line.split(",", 9)[-1]
                print(dialogue_text)
            elif in_dialogue_section and line.startswith("Format:"):
                # End of dialogue section
                in_dialogue_section = False

# Run the script
extract_dialogue(subtitles_file_path)
