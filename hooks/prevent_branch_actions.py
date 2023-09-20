import argparse
import subprocess
import sys


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prevent actions to specific branches")

    parser.add_argument(
        dest="branches",
        action="store",
        nargs="*",
        default=["main", "master"],
        type=str,
        help="Branches to prevent the action. Defaults to ' ['main', 'master'] '",
    )

    return parser


def _parse_branches(args: list[str], parser: argparse.ArgumentParser) -> set[str]:
    namespace = parser.parse_args(args=args)

    return set(namespace.branches)


def _get_current_branch() -> str:
    result = subprocess.run(
        args=["git", "rev-parse", "--abbrev-ref", "HEAD"],
        check=True,
        capture_output=True,
    )

    return result.stdout.decode().strip()


def _prevent_branch_actions(args: list[str]):
    parser = _parser()

    branches = _parse_branches(args=args, parser=parser)

    current_branch = _get_current_branch()

    if current_branch in branches:
        raise ValueError(f"can't perform actions on '{current_branch}'")


def main(args: list[str]) -> None:
    _prevent_branch_actions(args)


if __name__ == "__main__":
    main(sys.argv[1:])
