class MockResult:
    def __init__(self, stdout: bytes) -> None:
        self._stdout = stdout

    @property
    def stdout(self) -> bytes:
        return self._stdout
