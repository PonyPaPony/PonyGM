import pytest
from pony_git.exceptions import GitManagerError
from pony_git.validators import ensure_git_repo, is_git_repo_present, is_gitignore_present, ensure_gitignore


def test_is_git_repo_present_basic(git_repo):
    """Тест: 1.1 Проверяем работу функции is_git_repo_present"""
    assert is_git_repo_present() is True

def test_is_git_repo_present_empty_dir(empty_dir):
    """Тест: 1.2 Проверяем работу функции is_git_repo_present в пустом каталоге"""
    assert is_git_repo_present() is False

def test_is_gitignore_present_basic(git_repo_with_gitignore):
    """Тест: 1.3 Проверяем работу функции is_gitignore_present"""
    assert is_gitignore_present() is True

def test_is_gitignore_present_without_gitignore(git_repo):
    """Тест: 1.4 Проверяем работу функции is_gitignore_present в пустом каталоге"""
    assert is_gitignore_present() is False

def test_ensure_git_repo_basic(empty_dir):
    """Тест: 1.5 Проверяем работу функции ensure_git_repo"""
    with pytest.raises(GitManagerError, match="Git repository not found"):
        ensure_git_repo()

def test_ensure_gitignore_basic(git_repo):
    """Тест: 1.6 Проверяем работу функции ensure_gitignore"""
    with pytest.raises(GitManagerError, match='.gitignore not found'):
        ensure_gitignore()