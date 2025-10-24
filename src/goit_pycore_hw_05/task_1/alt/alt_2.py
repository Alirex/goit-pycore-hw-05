from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_1.typing import (
        T_CACHING_FIBONACCI_CALLABLE,
        T_FIBONACCI_NUMBER_INDEX,
        T_FIBONACCI_NUMBER_VALUE,
    )


def cacheable_fibonacci_without_recursion() -> T_CACHING_FIBONACCI_CALLABLE:
    cache: dict[T_FIBONACCI_NUMBER_INDEX, T_FIBONACCI_NUMBER_VALUE] = {
        0: 0,
        1: 1,
    }

    def fibonacci(number: T_FIBONACCI_NUMBER_INDEX) -> T_FIBONACCI_NUMBER_VALUE:
        if number < 0:
            msg = "Incorrect input value"
            raise ValueError(msg)

        if number in cache:
            return cache[number]

        max_number = max(cache.keys())
        for index in range(max_number + 1, number + 1):
            cache[index] = cache[index - 1] + cache[index - 2]

        return cache[number]

    return fibonacci
