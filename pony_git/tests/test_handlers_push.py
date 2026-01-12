import pytest
from types import SimpleNamespace
from pony_git.handlers import handler_push
from pony_git.exceptions import GitManagerError


def test_handler_push_basic(git_repo, capture_run_cmd):
    """Тест: 1.1 Проверяем работу push без tags"""
    args = SimpleNamespace(tags=False)
    handler_push(args)

    assert capture_run_cmd == [['git', 'push']]


def test_handler_push_with_tags(git_repo, capture_run_cmd):
    """Тест: 1.2 Проверяем работу push с tags"""
    args = SimpleNamespace(tags=True)
    handler_push(args)

    assert capture_run_cmd == [['git', 'push', '--tags']]

def test_handler_push_without_git_repo(empty_dir, forbid_run_cmd):
    """Тест: 1.3 Проверяем работу push без git репозитория"""
    args = SimpleNamespace(tags=False)
    with pytest.raises(GitManagerError):
        handler_push(args)