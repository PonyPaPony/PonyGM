import pytest
from types import SimpleNamespace
from unittest.mock import patch
from pony_git.handlers import handler_remove
from pony_git.exceptions import GitManagerError


def test_handler_remove_basic(git_repo, capture_run_cmd):
    """Тест 1.1 Проверяем базовый сценарий работы handler_remove"""
    args = SimpleNamespace(file='test_file.txt', force=False)
    handler_remove(args)
    assert capture_run_cmd == [['git', 'rm', '--cached', '-f', 'test_file.txt']]

def test_handler_remove_force(git_repo, capture_run_cmd):
    """Тест 1.2 Проверяем работу handler_remove с параметром force=True"""
    args = SimpleNamespace(file="test_file.txt", force=True)
    handler_remove(args)
    assert capture_run_cmd == [['git', 'rm', '-f', 'test_file.txt']]

@pytest.mark.parametrize(
    "file, force",
    [("test_file.txt", True),
     ("test_file.txt", False)]
)
def test_handler_remove_without_git_repo(empty_dir, forbid_run_cmd, file, force):
    """Тест 1.3 Проверяем работу handler_remove без git репозитория"""
    args = SimpleNamespace(file=file, force=force)
    with pytest.raises(GitManagerError):
        handler_remove(args)

@patch('pony_git.handlers.run_cmd', side_effect=GitManagerError("test error"))
def test_handler_remove_err_status(mock_run_cmd, git_repo):
    """Тест 1.5 Проверяем работу handler_remove с ошибкой GitManagerError"""
    with pytest.raises(GitManagerError, match="test error"):
        handler_remove(SimpleNamespace(file="test_file.txt", force=True))
    mock_run_cmd.assert_called_once()