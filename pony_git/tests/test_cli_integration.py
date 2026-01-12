import sys
import subprocess
import pytest
from pony_git.parsers.builder import build_parser
from pony_git.main import main


def test_cli_remove_calls_run_cmd(git_repo, monkeypatch):
    """Тест 1.1
    Интеграционный тест (parser -> handler).
    Проверяем, что CLI-команда `remove <file>`:
    - корректно парсится через build_parser()
    - приводит к вызову handlers.run_cmd с ожидаемой командой git
    - по умолчанию использует check=True"""
    calls = []

    def fake_run_cmd(cmd, check=True):
        calls.append((cmd, check))

    monkeypatch.setattr("pony_git.handlers.run_cmd", fake_run_cmd)

    parser = build_parser()
    args = parser.parse_args(['remove', 'test_file.txt'])

    args.func(args)

    assert calls == [(['git', 'rm', '--cached', '-f', 'test_file.txt'], True)]


def test_main_exit_code_when_no_git_repo(empty_dir, monkeypatch, capsys):
    """Тест 1.2
    Интеграционный тест (main -> обработка ошибок).
    Проверяем, что при запуске `pony-git status` вне git-репозитория:
    - main() завершает выполнение с кодом 1 (SystemExit(1))
    - сообщение об ошибке выводится пользователю (stderr)"""
    monkeypatch.setattr("sys.argv", ['pony-git', 'status'])

    with pytest.raises(SystemExit) as e:
        main()

    assert e.value.code == 1

    captured = capsys.readouterr()
    assert "Git repository not found" in captured.err


def test_python_m_pony_git_shows_help():
    """Тест 1.3
    Интеграционный тест entrypoint (python -m pony_git).
    Проверяем, что пакет запускается как модуль:
    - команда `python -m pony_git --help` возвращает код 0
    - help/usage выводится в stdout"""
    result = subprocess.run(
        [sys.executable, "-m", "pony_git", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "pony-git" in result.stdout.lower()