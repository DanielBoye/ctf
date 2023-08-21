import subprocess
import random
import string
import re
import string
import random

def generate_random_string_flag():
    characters = string.ascii_letters + string.digits + '_!?#.:*\-'
    length = random.randint(8, 32)
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_string():
    characters = string.ascii_letters + string.digits + '_!?#.:*\-'
    extra = ['%', '|', '§', '`']
    length = random.randint(8, 32)
    
    random_string = ''.join(random.choice(characters) for _ in range(length))
    random_position = random.randint(0, length)  # Random position to insert the extra character
    random_extra_character = random.choice(extra)
    
    # Insert the random extra character at the random position within the random string
    random_string_with_extra = random_string[:random_position] + random_extra_character + random_string[random_position:]
    
    return random_string_with_extra

def make_git_commits(num_commits):
    try:
        for i in range(1, num_commits + 1):
            if i == 7632:
                prefix = "ctf{"
                random_length = random.randint(8, 32)
                commit_name = generate_random_string_flag()
            else:
                prefix = "ctf{"
                random_length = random.randint(8, 32)
                commit_name = generate_random_string()

            commit_description = f"{prefix}{commit_name}" + "}"

            subprocess.run(['git', 'commit', '--allow-empty', '-m', commit_description, '--allow-empty-message', '--no-verify'], env={'GIT_COMMITTER_NAME': commit_name, 'GIT_COMMITTER_EMAIL': 'noreply@example.com'})
    except KeyboardInterrupt:
        print("\nScript interrupted by user. Exiting gracefully.")

if __name__ == '__main__':
    num_commits = 10000
    make_git_commits(num_commits)
