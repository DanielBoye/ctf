# get_good

## Daniel Boye

## Category: {Forensics, Misc}

## Problem Statement

This is a challenge where the user need to find the right flag in the commit history. And there are 10 000 commits. They can list the logs with `git log` but will soon find out that all of the flags looks the same! That is why knowing regex is important. The learning objective for this challenge is to learn to filter information based on regex with the use of the command `grep`. And don't let grep fool you, since you can't accually just paste in the regex as is. You need to have some extra characters such as `\` a few places and search with `^`. We need to use the caret symbol since it specifies that we want to search to things that starts with a new line. 

The backlashes used here `\{8,32\}` is also needed since it specifies the allowed length of characters inside the curly braces. It means the pattern inside the curly braces should be repeated between 8 and 32 times.


For extra you can add to the solve command with learning how to format and print out only the specified flag with adding a `--format=%B` since %B is a placeholder that represents the commit message body and using pipe `|` and a new `grep` for printing the matching part of the line.

## Flavor Text

wtf! there are flags in my drivers! 
but wait, I think this character will help me: ^

Flag format: Same as ECSC, just with ctf as a prefix!

## Difficulty

- **Easy:** 1-5 steps, typically 2-5


## Challenge Information (2/3)

- **Estimated Solve Time:** 5min-60min
- **Solver Script:** 

```bash
#!/usr/bin/env bash

git log --grep '^ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}' -p --format=%B | grep -o '^ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}'
```
## Type

- **Downloadable Artifacts:** See zip file attatched in the email. 

## Solution description

1. Find the regex provided to the participants: `ECSC{[a-zA-Z0-9_!?#.:*\-]{8,32}}}`

2. See that the prefix for the flag is `ctf`

3. Edit the regex to the flag format

4. Sort for commits with that regex 
`git log --grep '^ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}'`

There you have the flag!

Additional steps for styling:

5. Print out just the flag
`git log --grep '^ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}' -p --format=%B | grep -o '^ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}'`

6. Make solvescript
solve.sh
```bash
#!/usr/bin/env bash

git log --grep '^ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}' -p --format=%B | grep -o '^ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}'
```

## Extra

### How I made it

1. Copied the drivers from a xritecolorassistant 

2. Then made a bash script that removes any previous `.git` and adds a motivating email and username to the author that will commit the flags

```bash
#!/usr/bin/env bash

rm -rf .git
git init

git config user.email "very@closetotheflag.com"
git config user.name "youaregetting"
```

3. Then made this file that injects all of the flags into commits that are committed

```python
import subprocess
import random
import string
import re

def generate_random_string():
    characters = string.ascii_letters + string.digits + '_!?#.:*\-'
    length = random.randint(8, 32)
    return ''.join(random.choice(characters) for _ in range(length))

def make_git_commits(num_commits):
    try:
        for i in range(1, num_commits + 1):
            if i == 7632:
                prefix = "ctf{"
                random_length = random.randint(8, 32)
                commit_name = generate_random_string()
            else:
                prefix = "ctf{"
                random_length = random.randint(8, 31)
                commit_name = generate_random_string() + "%"

            commit_description = f"{prefix}{commit_name}" + "}"

            subprocess.run(['git', 'commit', '--allow-empty', '-m', commit_description, '--allow-empty-message', '--no-verify'], env={'GIT_COMMITTER_NAME': commit_name, 'GIT_COMMITTER_EMAIL': 'noreply@example.com'})

    except KeyboardInterrupt:
        print("\nScript interrupted by user. Exiting gracefully.")

if __name__ == '__main__':
    num_commits = 10000
    make_git_commits(num_commits)
```

