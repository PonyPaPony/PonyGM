import pytest
from types import SimpleNamespace
from pony_git.handlers import handler_add
from pony_git.exceptions import GitManagerError


def test_handler_add_without_force_and_without_gitignore(git_repo, forbid_run_cmd):
    """Тест: 1.1 Проверяем работу add без gitignore и --force"""
    args = SimpleNamespace(m='test-commit', force=False)

    with pytest.raises(GitManagerError, match='.gitignore not found. Use --force to proceed.'):
        handler_add(args)

def test_handler_add_with_force_and_without_gitignore(git_repo, capture_run_cmd, capsys):
    """Тест: 1.2 Проверяем работу add без gitignore"""
    args = SimpleNamespace(m='test-commit', force=True)

    handler_add(args)

    captured = capsys.readouterr()
    assert "Warning: .gitignore not found" in captured.err

def test_handler_add_with_gitignore(git_repo_with_gitignore, capture_run_cmd):
    """Тест: 1.3 Проверяем работу add с gitignore"""
    args = SimpleNamespace(m='test-commit', force=False)
    handler_add(args)
    assert capture_run_cmd[0] == ['git', 'add', '.']
    assert capture_run_cmd[1] == ['git', 'commit', '-m', 'test-commit']

def test_handler_add_without_m_tag(git_repo, capture_run_cmd):
    """Тест: 1.4 Проверяем работу add без -m"""
    args = SimpleNamespace(m=None, force=False)
    with pytest.raises(GitManagerError):
        handler_add(args)

    assert capture_run_cmd == []

def test_handler_without_git_repo(empty_dir, forbid_run_cmd):
    """Тест: 1.5 Проверяем работу add без git-репозитория"""
    args = SimpleNamespace(m='test-commit', force=False)
    with pytest.raises(GitManagerError, match="Git repository not found"):
        handler_add(args)