CMD_COMMANDS = {
    'init': ['git', 'init'],
    'add': ['git', 'add', '.'],
    "commit": ['git', 'commit', '-m'],
    "push_main": ['git', 'push'],
    "push_main_upstream": ['git', 'push', '-u', 'origin', 'main'],
    'push_tag': ['git', 'push', '--tags'],
    'branch': ['git', 'branch', '-M'],
    "remote": ['git', "remote"],
    "tag": ['git', 'tag'],
    'version': ['git', '--version'],
    'status': ['git', 'status'],
    'remove': ['git', 'rm'],
}

INFO_FIRST_PUSH = """
First push (pony-git workflow):

1. pony-git init
2. pony-git add -m "Initial commit"
3. pony-git branch -M <branch-name> # Usually 'main' or 'master'
4. pony-git remote add origin <URL>
5. pony-git tag -a vX.Y.Z -m "Release message"   (optional)
6. pony-git push -M        # First push to main
7. pony-git push -T        # Push tags (if created)

Tip:
- Use 'pony-git push -M' for first push to main
- Use 'pony-git push' for subsequent pushes
- Make sure .gitignore exists before pony-git add
"""

INFO_UPDATE = """
Update workflow (pony-git):

1. pony-git status
2. pony-git add -m "Your message"
3. pony-git tag -a vX.Y.Z -m "Release message"   (optional)
4. pony-git push
5. pony-git push --tags   (if you created a tag)
"""