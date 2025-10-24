from typing import Any, Final

TEXT_MAX_LENGTH: Final[int] = 10


def generate_id(
    param: Any,  # noqa: ANN401
) -> object | None:
    if isinstance(param, str):
        return f"{param[:TEXT_MAX_LENGTH]}..." if len(param) > TEXT_MAX_LENGTH else param
    return None
