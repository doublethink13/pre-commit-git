# pre-commit-git

A repository with git related hooks. Developed with `pre-commit` in mind.

## prevent_branch_actions

A hook to prevent commit/push actions on certain branches (main and master by default).

Usage:

```bash
$ python ./hooks/prevent_branch_actions.py --help
usage: prevent.py [-h] [branches]

Prevent actions to specific branches

positional arguments:
  branches    Branches to prevent the action. Defaults to ' ['main', 'master'] '

options:
  -h, --help  show this help message and exit
```

With `pre-commit`:

```yaml
---
# default for all hooks' stages in this repo
default_install_hook_types:
  - pre-commit
  - pre-push
repos:
  - hooks:
      - always_run: true
        # by default args is ["main", "master"]
        # see usage above
        args:
          - add-pre-commit-config
        id: prevent
    repo: https://github.com/doublethink13/pre-commit-git
    # check https://github.com/doublethink13/pre-commit-git/tags for latest revision
    rev: 0.0.1
```

## Local development

Please check `make` usage:

```bash
$ make
Usage
        usage (default)
        usage setup_python_interpreter
        usage setup_venv
        usage install_requirements
        usage apply_formatting
        usage lint
```
