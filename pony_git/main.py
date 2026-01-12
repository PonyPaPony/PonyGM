import sys
from pony_git.parsers.builder import build_parser
from pony_git.exceptions import GitManagerError


def main():
    parser = build_parser()

    args = parser.parse_args()
    try:
        args.func(args)
    except GitManagerError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()