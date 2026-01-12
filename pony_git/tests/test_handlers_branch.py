import pytest
from types import SimpleNamespace
from pony_git.handlers import handler_branch
from pony_git.exceptions import GitManagerError


def test_branch_handler_basic(git_repo, capture_run_cmd):
    """Тест: 1.1 Проверяем работу branch с указанием имени ветки"""
    args = SimpleNamespace(M='main')
    handler_branch(args)

    assert capture_run_cmd == [['git', 'branch', 'main']]

def test_branch_handler_without_git_repo(empty_dir, forbid_run_cmd):
    """Тест: 1.2 Проверяем работу branch без git репозитория"""
    args = SimpleNamespace(M='main')
    with pytest.raises(GitManagerError):
        handler_branch(args)