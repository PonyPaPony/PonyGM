import argparse

def add_commit_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-m", type=str, required=True, help="Commit message")
    parser.add_argument('--force', action='store_true', help='Force commit')


def add_push_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-T", "--tags", action="store_true", help="Push tag")
    parser.add_argument('-M', '--main', action='store_true', help='Push to main with upstream')


def add_branch_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-M", type=str, required=True, help="Branch name")


def add_remote_list_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-v",
        action="store_true",
        help="Show remote URLs",
    )


def add_remote_add_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("name", help="Remote name")
    parser.add_argument("url", help="Remote URL")


def add_remote_remove_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("name", help="Remote name")


def add_tag_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-a", type=str, required=True, help="Tag name")
    parser.add_argument("-m", type=str, required=True, help="Tag message")

def add_info_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-u", '--update', action='store_true', help='Update info')

def add_status_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('-p', '--porcelain', action='store_true', help='Show porcelain output')

def add_remove_parser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument('file', help='File to remove')
    parser.add_argument("--force", action="store_true", help="Force remove")