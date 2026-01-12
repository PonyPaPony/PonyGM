import pytest
from types import SimpleNamespace
from pony_git.handlers import handler_init
from pony_git.exceptions import GitManagerError


def test_handler_init_when_git_repo_already_exists(git_repo, forbid_run_cmd):
    """Тест: 1.1 Проверяем работу init при уже существующем git репозитории"""
    args = SimpleNamespace()
    with pytest.raises(GitManagerError):
        handler_init(args)

def test_handler_init_when_git_repo_not_exists(empty_dir, capture_run_cmd):
    """Тест: 1.2 Проверяем работу init при отсутствии git репозитория"""
    args = SimpleNamespace()
    handler_init(args)

    assert capture_run_cmd == [['git', 'init']]