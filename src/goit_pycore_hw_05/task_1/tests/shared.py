from typing import Final, TypeAlias

T_PARAMS_NAMES: TypeAlias = tuple[str, ...]
T_VALUES: TypeAlias = tuple[int, int]
T_VALUES_SEQUENCE: TypeAlias = tuple[T_VALUES, ...]

PARAMETRIZE_FIXTURE: Final[tuple[T_PARAMS_NAMES, T_VALUES_SEQUENCE]] = (
    ("index", "value"),
    (
        (10, 55),
        (15, 610),
        (20, 6765),
    ),
)
