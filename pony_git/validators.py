from pathlib import Path
from pony_git.exceptions import GitManagerError

def get_git_dir():
    return Path.cwd().resolve() / '.git'

def get_gitignore_path():
    return Path.cwd().resolve() / '.gitignore'

def is_git_repo_present() -> bool:
    git_dir = get_git_dir()
    return git_dir.exists() and git_dir.is_dir()


def is_gitignore_present() -> bool:
    gitignore = get_gitignore_path()
    return gitignore.exists() and gitignore.is_file()


def ensure_git_repo():
    if not is_git_repo_present():
        raise GitManagerError("Git repository not found")


def ensure_gitignore():
    if not is_gitignore_present():
        raise GitManagerError(".gitignore not found")