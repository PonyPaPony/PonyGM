from types import SimpleNamespace
from pony_git.handlers import handler_check_version


def test_handler_check_version(capture_run_cmd, empty_dir):
    """Тест: 1.1 Проверяем работу команды version"""
    args = SimpleNamespace()
    handler_check_version(args)

    assert capture_run_cmd == [['git', '--version']]