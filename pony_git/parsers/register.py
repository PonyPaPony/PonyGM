import argparse

from pony_git.handlers import (
    handler_add,
    handler_branch,
    handler_check_version,
    handler_init,
    handler_push,
    handler_remote_add,
    handler_remote_list,
    handler_remote_remove,
    handler_tag,
    handler_info,
    handler_status,
    handler_remove,
)

from pony_git.parsers.arguments import (
    add_branch_parser,
    add_commit_parser,
    add_push_parser,
    add_remote_add_parser,
    add_remote_list_parser,
    add_remote_remove_parser,
    add_tag_parser,
    add_info_parser,
    add_status_parser,
    add_remove_parser,
)


def register_push(subparsers: argparse._SubParsersAction) -> None:
    push = subparsers.add_parser(
        "push",
        help="Push changes to remote",
    )

    add_push_parser(push)
    push.set_defaults(func=handler_push)


def register_remote(subparsers: argparse._SubParsersAction) -> None:
    remote = subparsers.add_parser(
        "remote",
        help="Manage git remotes",
    )

    remote_sub = remote.add_subparsers(
        dest="action",
        required=True,
    )

    # remote list
    remote_list = remote_sub.add_parser(
        "list",
        help="List remotes",
    )
    add_remote_list_parser(remote_list)
    remote_list.set_defaults(func=handler_remote_list)

    # remote add
    remote_add = remote_sub.add_parser(
        "add",
        help="Add remote",
    )
    add_remote_add_parser(remote_add)
    remote_add.set_defaults(func=handler_remote_add)

    # remote remove
    remote_remove = remote_sub.add_parser(
        "remove",
        help="Remove remote",
    )
    add_remote_remove_parser(remote_remove)
    remote_remove.set_defaults(func=handler_remote_remove)


def register_add(subparsers: argparse._SubParsersAction) -> None:
    add = subparsers.add_parser(
        "add",
        help="Add files and commit",
    )
    add_commit_parser(add)
    add.set_defaults(func=handler_add)


def register_init(subparsers: argparse._SubParsersAction) -> None:
    init = subparsers.add_parser(
        "init",
        help="Initialize git repository",
    )
    init.set_defaults(func=handler_init)


def register_branch(subparsers: argparse._SubParsersAction) -> None:
    branch = subparsers.add_parser(
        "branch",
        help="Create new branch",
    )
    add_branch_parser(branch)
    branch.set_defaults(func=handler_branch)


def register_tag(subparsers: argparse._SubParsersAction) -> None:
    tag = subparsers.add_parser(
        "tag",
        help="Create new tag",
    )
    add_tag_parser(tag)
    tag.set_defaults(func=handler_tag)


def register_version(subparsers: argparse._SubParsersAction) -> None:
    version = subparsers.add_parser(
        "version",
        help="Show pony-git version",
    )
    version.set_defaults(func=handler_check_version)

def register_info(subparsers: argparse._SubParsersAction) -> None:
    info = subparsers.add_parser(
        "info",
        help="Show recommended pony-git workflows",
    )
    add_info_parser(info)
    info.set_defaults(func=handler_info)

def register_status(subparsers: argparse._SubParsersAction) -> None:
    status = subparsers.add_parser(
        "status",
        help="Show git status",
    )
    add_status_parser(status)
    status.set_defaults(func=handler_status)

def register_remove(subparsers: argparse._SubParsersAction) -> None:
    remove = subparsers.add_parser(
        "remove",
        help="Remove files from git",
    )
    add_remove_parser(remove)
    remove.set_defaults(func=handler_remove)