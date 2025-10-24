import pytest

from goit_pycore_hw_05.task_1.alt.alt_1 import cacheable_fibonacci_with_decorator_and_recursion
from goit_pycore_hw_05.task_1.tests.shared import PARAMETRIZE_FIXTURE


@pytest.mark.parametrize(*PARAMETRIZE_FIXTURE)
def test_fibonaci(
    index: int,
    value: int,
) -> None:
    result = cacheable_fibonacci_with_decorator_and_recursion(index)
    assert result == value
