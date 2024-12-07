from textwrap import dedent


class UnreachableCodeError(AssertionError):
    """Mark a branch as unreachable.

    This is to aid static analysers.
    """

    def __init__(self) -> None:
        doc = dedent(self.__doc__ or "")
        super().__init__(doc)
