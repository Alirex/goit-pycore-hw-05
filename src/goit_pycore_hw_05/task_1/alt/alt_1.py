import functools
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_1.typing import T_FIBONACCI_NUMBER_INDEX, T_FIBONACCI_NUMBER_VALUE


@functools.cache
def cacheable_fibonacci_with_decorator_and_recursion(number: T_FIBONACCI_NUMBER_INDEX) -> T_FIBONACCI_NUMBER_VALUE:
    if number < 0:
        msg = "Incorrect input value"
        raise ValueError(msg)

    if number in {0, 1}:
        return number

    return cacheable_fibonacci_with_decorator_and_recursion(
        number - 1,
    ) + cacheable_fibonacci_with_decorator_and_recursion(number - 2)
