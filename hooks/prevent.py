import argparse
import subprocess


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prevent actions to specific branches")

    parser.add_argument(
        dest="branches",
        action="append",
        nargs="?",
        default=["main", "master"],
        type=str,
        help="Branches to prevent the action. Defaults to ' ['main', 'master'] '",
    )

    return parser


def _parse_branches(parser: argparse.ArgumentParser) -> set[str]:
    namespace = parser.parse_args()

    return set(namespace.branches)


def _get_current_branch() -> str:
    result = subprocess.run(
        args=["git", "rev-parse", "--abbrev-ref", "HEAD"],
        check=True,
        capture_output=True,
    )

    return result.stdout.decode().strip()


def _prevent():
    parser = _parser()

    branches = _parse_branches(parser=parser)

    current_branch = _get_current_branch()

    if current_branch in branches:
        raise ValueError(f"can't perform actions on '{current_branch}'")


def main() -> None:
    _prevent()


if __name__ == "__main__":
    main()