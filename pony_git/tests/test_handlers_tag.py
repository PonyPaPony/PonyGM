import pytest
from types import SimpleNamespace
from pony_git.handlers import handler_tag
from pony_git.exceptions import GitManagerError


def test_tag_handler_basic(git_repo, capture_run_cmd):
    """Тест: 1.1 Проверяем работу tag с указанием имени тега"""
    args = SimpleNamespace(a='v1.0.0', m='Initial release')
    handler_tag(args)

    assert capture_run_cmd == [['git', 'tag', '-a', 'v1.0.0', '-m', 'Initial release']]

def test_tag_handler_without_git_repo(empty_dir, forbid_run_cmd):
    """Тест: 1.2 Проверяем работу tag без git репозитория"""
    args = SimpleNamespace(a='v1.0.0', m='Initial release')
    with pytest.raises(GitManagerError):
        handler_tag(args)
