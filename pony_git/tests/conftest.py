import pytest


@pytest.fixture
def git_repo(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".git").mkdir()
    return tmp_path

@pytest.fixture
def git_repo_with_gitignore(git_repo):
    (git_repo / ".gitignore").write_text("*.pyc\n")
    return git_repo

@pytest.fixture
def empty_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path

@pytest.fixture
def forbid_run_cmd(monkeypatch):
    def fake_run_cmd(cmd, check=True):
        pytest.fail("run_cmd should not be called")

    monkeypatch.setattr("pony_git.handlers.run_cmd", fake_run_cmd)

@pytest.fixture
def capture_run_cmd(monkeypatch):
    calls = []

    def fake_run_cmd(cmd, check=True):
        calls.append(cmd)

    monkeypatch.setattr("pony_git.handlers.run_cmd", fake_run_cmd)
    return calls

@pytest.fixture()
def fake_sub_run(monkeypatch):
    calls = []
    def fake_run_cmd(cmd, check=True):
        calls.append((cmd, check))

    monkeypatch.setattr('subprocess.run', fake_run_cmd)
    return calls