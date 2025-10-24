from collections.abc import Callable
from typing import TypeAlias

T_FIBONACCI_NUMBER_INDEX: TypeAlias = int
T_FIBONACCI_NUMBER_VALUE: TypeAlias = int
T_CACHING_FIBONACCI_CALLABLE: TypeAlias = Callable[[T_FIBONACCI_NUMBER_INDEX], T_FIBONACCI_NUMBER_VALUE]
