import pytest
from types import SimpleNamespace

from pony_git.exceptions import GitManagerError
from pony_git.handlers import handler_status


def test_handler_status_basic(git_repo_with_gitignore, capture_run_cmd):
    """Тест 1.1 Проверяем базовый сценарий работы handler_status"""
    args = SimpleNamespace(porcelain=False)
    handler_status(args)

    assert capture_run_cmd == [['git', 'status', '--short']]

def test_handler_status_porcelain(git_repo_with_gitignore, capture_run_cmd):
    """Тест 1.2 Проверяем работу handler_status с параметром porcelain=True"""
    args = SimpleNamespace(porcelain=True)
    handler_status(args)

    assert capture_run_cmd == [['git', 'status', '--porcelain']]

def test_handler_status_without_git_repo(empty_dir, forbid_run_cmd):
    """Тест 1.3 Проверяем работу handler_status без git репозитория"""
    args = SimpleNamespace(porcelain=False)
    with pytest.raises(GitManagerError):
        handler_status(args)

@pytest.mark.parametrize("porcelain, expected", [(True, ['git', 'status', '--porcelain']),
                                                 (False, ['git', 'status', '--short'])])
def test_handler_status_warning(git_repo, capture_run_cmd, capsys, porcelain, expected):
    """Тест 1.4 Проверяем вывод предупреждения при отсутствии .gitignore"""
    args = SimpleNamespace(porcelain=porcelain)
    handler_status(args)

    captured = capsys.readouterr()
    assert "Warning: .gitignore not found" in captured.err
    assert capture_run_cmd == [expected]