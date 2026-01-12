import argparse

from pony_git.parsers.register import (
    register_add,
    register_branch,
    register_init,
    register_push,
    register_remote,
    register_tag,
    register_version,
    register_info,
    register_status,
    register_remove,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pony-git",
        description="Git manager CLI",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    register_init(subparsers)
    register_add(subparsers)
    register_push(subparsers)
    register_branch(subparsers)
    register_remote(subparsers)
    register_tag(subparsers)
    register_version(subparsers)
    register_info(subparsers)
    register_status(subparsers)
    register_remove(subparsers)

    return parser