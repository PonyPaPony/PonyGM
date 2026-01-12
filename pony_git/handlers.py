import sys
from pony_git.validators import is_git_repo_present, ensure_git_repo, is_gitignore_present
from pony_git.runner import run_cmd
from pony_git.exceptions import GitManagerError
from pony_git.config import CMD_COMMANDS, INFO_UPDATE, INFO_FIRST_PUSH

def handler_init(args):
    if is_git_repo_present():
        raise GitManagerError("Git repository already exists")
    run_cmd(CMD_COMMANDS['init'])


def handler_add(args):
    ensure_git_repo()

    if not is_gitignore_present() and not args.force:
        raise GitManagerError(".gitignore not found. Use --force to proceed.")
    if not is_gitignore_present() and args.force:
        print("Warning: .gitignore not found, proceeding due to --force", file=sys.stderr)

    run_cmd(CMD_COMMANDS['add'])
    run_cmd(CMD_COMMANDS['commit'] + [args.m])

def handler_push(args):
    ensure_git_repo()
    if args.tags:
        cmd = CMD_COMMANDS['push_tag']
    elif args.main:
        cmd = CMD_COMMANDS['push_main_upstream']
    else:
        cmd = CMD_COMMANDS['push_main']
    run_cmd(cmd)

def handler_branch(args):
    ensure_git_repo()
    run_cmd(CMD_COMMANDS['branch'] + [args.M])

def handler_remote_list(args):
    ensure_git_repo()
    cmd = CMD_COMMANDS['remote']
    if args.v:
        cmd  = cmd + ['-v']
    run_cmd(cmd)


def handler_remote_add(args):
    ensure_git_repo()
    run_cmd(CMD_COMMANDS['remote'] + ['add', args.name, args.url])

def handler_remote_remove(args):
    ensure_git_repo()
    run_cmd(CMD_COMMANDS['remote'] + ['remove', args.name])

def handler_tag(args):
    ensure_git_repo()
    cmd = CMD_COMMANDS['tag'] + ['-a'] + [args.a] + ['-m'] +[args.m]
    run_cmd(cmd)

def handler_check_version(args):
    run_cmd(CMD_COMMANDS['version'])

def handler_info(args):
    print(INFO_UPDATE if args.update else INFO_FIRST_PUSH)

def handler_status(args):
    ensure_git_repo()

    if not is_gitignore_present():
        print("Warning: .gitignore not found", file=sys.stderr)

    if not args.porcelain:
        cmd = CMD_COMMANDS['status'] + ['--short']
    else:
        cmd = CMD_COMMANDS['status'] + ['--porcelain']

    run_cmd(cmd)

def handler_remove(args):
    ensure_git_repo()

    cmd = (
        CMD_COMMANDS["remove"] + ["-f", args.file]
        if args.force
        else CMD_COMMANDS["remove"] + ["--cached", "-f", args.file]
    )

    run_cmd(cmd)