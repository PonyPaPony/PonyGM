
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-12

### Added

#### Core Functionality
- **CLI Framework**: Полнофункциональный интерфейс командной строки для управления Git
- **Модульная архитектура**: Разделение на parsers, handlers, validators и runners
- **Обработка ошибок**: Кастомное исключение `GitManagerError` для централизованной обработки ошибок

#### Git Commands
- `pony-git init` - инициализация нового Git-репозитория
- `pony-git add -m <message>` - добавление файлов и создание коммита с поддержкой `--force`
- `pony-git push` - отправка изменений в удалённый репозиторий с опцией `--tags`
- `pony-git branch -M <name>` - создание новой ветки
- `pony-git tag -a <name> -m <message>` - создание аннотированного тега
- `pony-git status` - отображение статуса репозитория с опциями `--short` и `--porcelain`
- `pony-git remove <file>` - удаление файлов из индекса Git (по умолчанию) с возможностью физического удаления через `--force`
- `pony-git version` - отображение версии Git

#### Remote Management
- `pony-git remote list` - просмотр удалённых репозиториев с опцией `-v`
- `pony-git remote add <name> <url>` - добавление удалённого репозитория
- `pony-git remote remove <name>` - удаление удалённого репозитория

#### Workflow Helpers
- `pony-git info` - отображение рекомендуемых рабочих процессов (первый push)
- `pony-git info --update` - отображение процесса обновления проекта

#### Safety Features
- Проверка наличия `.gitignore` перед операциями add/status с предупреждениями
- Валидация наличия Git-репозитория перед выполнением команд
- Опция `--force` для обхода проверки `.gitignore`
- Корректная обработка ошибок Git с понятными сообщениями

#### Testing
- **Обширное покрытие тестами**: 100+ unit и integration тестов
- Тестирование всех handlers (add, branch, init, push, remote, remove, status, tag, version, info)
- Интеграционные тесты CLI через `python -m pony_git`
- Тестирование обработки ошибок и edge cases
- Fixtures для изолированного тестирования (git_repo, empty_dir, capture_run_cmd)

#### Documentation
- Лицензия MIT
- Базовая структура README
- Конфигурация pyproject.toml с метаданными проекта

### Technical Details
- **Python Version**: >= 3.11
- **Dependencies**: pytest для разработки и тестирования
- **Package Manager**: virtualenv
- **Build System**: setuptools >= 61.0
- **Entry Point**: `pony-git` CLI command

### Project Structure