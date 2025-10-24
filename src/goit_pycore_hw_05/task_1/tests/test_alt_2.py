from typing import TYPE_CHECKING

import pytest

from goit_pycore_hw_05.task_1.alt.alt_2 import cacheable_fibonacci_without_recursion
from goit_pycore_hw_05.task_1.tests.shared import PARAMETRIZE_FIXTURE

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_1.typing import T_CACHING_FIBONACCI_CALLABLE


@pytest.fixture
def caching_fibonacci_fixture() -> T_CACHING_FIBONACCI_CALLABLE:
    return cacheable_fibonacci_without_recursion()


@pytest.mark.parametrize(*PARAMETRIZE_FIXTURE)
def test_fibonaci(
    index: int,
    value: int,
    caching_fibonacci_fixture: T_CACHING_FIBONACCI_CALLABLE,
) -> None:
    result = caching_fibonacci_fixture(index)
    assert result == value
