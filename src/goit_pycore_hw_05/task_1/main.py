from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_1.typing import (
        T_CACHING_FIBONACCI_CALLABLE,
        T_FIBONACCI_NUMBER_INDEX,
        T_FIBONACCI_NUMBER_VALUE,
    )


def caching_fibonacci() -> T_CACHING_FIBONACCI_CALLABLE:
    cache: dict[T_FIBONACCI_NUMBER_INDEX, T_FIBONACCI_NUMBER_VALUE] = {}

    def fibonacci(n: T_FIBONACCI_NUMBER_INDEX) -> T_FIBONACCI_NUMBER_VALUE:
        if n < 0:
            msg = "Incorrect input value"
            raise ValueError(msg)

        if n in {0, 1}:
            return n

        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci
