from unittest.mock import patch

import pytest

from hooks.prevent_branch_actions import main as prevent_branch_actions
from tests.mocks.result import MockResult


class TestPreventBranchActions:
    @pytest.mark.parametrize(
        ["args", "mock_result", "expect_error"],
        [
            ([], MockResult(stdout=b"main"), True),
            ([], MockResult(stdout=b"master"), True),
            ([], MockResult(stdout=b"test"), False),
            (["test"], MockResult(stdout=b"main"), False),
            (["test"], MockResult(stdout=b"master"), False),
            (["test"], MockResult(stdout=b"test"), True),
        ],
    )
    def test_prevent_branch_actions(
        self, args: list[str], mock_result: MockResult, expect_error: bool
    ) -> None:
        with patch("hooks.prevent_branch_actions.subprocess.run") as mock_run:
            mock_run.return_value = mock_result

            try:
                prevent_branch_actions(args)
            except ValueError:
                if not expect_error:
                    pytest.fail(reason="got error when none was expected")
            else:
                if expect_error:
                    pytest.fail(reason="expected an error but none was raised")
