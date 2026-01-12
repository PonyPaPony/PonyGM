from types import SimpleNamespace
from pony_git.handlers import handler_info
from pony_git.config import INFO_UPDATE, INFO_FIRST_PUSH


def test_handler_info(capsys):
    """Тест: 1.1 Проверяем работу команды info первый пуш"""
    args = SimpleNamespace(update=False)

    handler_info(args)

    captured = capsys.readouterr()
    assert INFO_FIRST_PUSH.strip() in captured.out

def test_handler_info_update(capsys):
    """Тест: 1.2 Проверяем работу команды info обновление"""
    args = SimpleNamespace(update=True)

    handler_info(args)

    captured = capsys.readouterr()
    assert INFO_UPDATE.strip() in captured.out