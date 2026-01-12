import pytest
from types import SimpleNamespace
from pony_git.handlers import handler_remote_add, handler_remote_list, handler_remote_remove
from pony_git.exceptions import GitManagerError


def test_handler_remote_list_basic(git_repo, capture_run_cmd):
    """Тест: 1.1 Проверяем работу команды remote list"""
    args = SimpleNamespace(v=True)
    handler_remote_list(args)

    assert capture_run_cmd == [['git', 'remote', '-v']]

def test_handler_remote_list_without_tag(git_repo, capture_run_cmd):
    """Тест: 1.2 Проверяем работу команды remote list без флага -v"""
    args = SimpleNamespace(v=False)
    handler_remote_list(args)

    assert capture_run_cmd == [['git', 'remote']]

def test_handler_remote_add(git_repo, capture_run_cmd):
    """Тест: 1.3 Проверяем работу команды remote add"""
    args = SimpleNamespace(name='origin', url='https://github.com/pony-git/pony-git.git')
    handler_remote_add(args)

    assert capture_run_cmd == [['git', 'remote', 'add', 'origin', 'https://github.com/pony-git/pony-git.git']]

def test_handler_remote_remove(git_repo, capture_run_cmd):
    """Тест: 1.4 Проверяем работу команды remote remove"""
    args = SimpleNamespace(name='origin')
    handler_remote_remove(args)

    assert capture_run_cmd == [['git', 'remote', 'remove', 'origin']]

def test_remote_list_without_git(empty_dir, forbid_run_cmd):
    """Тест: 1.5 Проверяем работу команды remote list без git"""
    args = SimpleNamespace(v=False)
    with pytest.raises(GitManagerError):
        handler_remote_list(args)


def test_remote_add_without_git(empty_dir, forbid_run_cmd):
    """Тест: 1.6 Проверяем работу команды remote add без git"""
    args = SimpleNamespace(name='origin', url='url')
    with pytest.raises(GitManagerError):
        handler_remote_add(args)


def test_remote_remove_without_git(empty_dir, forbid_run_cmd):
    """Тест: 1.7 Проверяем работу команды remote remove без git"""
    args = SimpleNamespace(name='origin')
    with pytest.raises(GitManagerError):
        handler_remote_remove(args)