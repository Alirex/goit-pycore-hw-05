import re
from decimal import Decimal
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Callable

    from goit_pycore_hw_05.task_2.typing import T_GENERATOR_NUMBERS, T_NUMBER

# Note: Don't look for negative numbers here. Because "profit" is always positive in this task.
# Note: Not used strict check for whitespaces ("\s*"). But, maybe, "boundary" ("\b") is enough.
PATTERN_I_DECIMAL_NUMBER_IN_TEXT: Final[re.Pattern[str]] = re.compile(
    r"""
\b              # Boundary
\d+             # Digits
(?:\.\d+)?      # Optional decimal part
\b              # Boundary
""",
    re.VERBOSE,
)


def generator_numbers(text: str) -> T_GENERATOR_NUMBERS:
    for number in PATTERN_I_DECIMAL_NUMBER_IN_TEXT.findall(text):
        yield Decimal(number)


def sum_profit(text: str, func: Callable[[str], T_GENERATOR_NUMBERS]) -> T_NUMBER:
    return sum(func(text), Decimal(0))
