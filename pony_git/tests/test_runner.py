import pytest
import subprocess
from pony_git.runner import run_cmd
from pony_git.exceptions import GitManagerError

def test_run_cmd(fake_sub_run):
    """Тест: 1.1 Проверяем работу функции run_cmd"""
    cmd = ['git', 'status']
    run_cmd(cmd)
    assert fake_sub_run == [(cmd, True)]

def test_run_cmd_failure(monkeypatch):
    """Тест: 1.2 Проверяем работу функции run_cmd при CalledProcessError"""
    def fake_run(cmd, check):
        raise subprocess.CalledProcessError(1, cmd)

    monkeypatch.setattr("subprocess.run", fake_run)

    with pytest.raises(GitManagerError):
        run_cmd(["git", "status"])

def test_run_cmd_check_false(fake_sub_run):
    """Тест: 1.3 Проверяем работу функции run_cmd с check=False"""
    run_cmd(["git", "status"], check=False)
    assert fake_sub_run == [(["git", "status"], False)]