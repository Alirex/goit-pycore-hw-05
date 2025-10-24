from decimal import Decimal

import pytest

from goit_pycore_hw_05.task_2.main import PATTERN_I_DECIMAL_NUMBER_IN_TEXT, generator_numbers, sum_profit
from goit_pycore_hw_05.task_2.tests.helpers import generate_id


@pytest.mark.parametrize(
    ("text", "values"),
    [
        ("1", ["1"]),
        ("1.2", ["1.2"]),
        ("The temperature is 23 degrees.", ["23"]),
        ("Pi is approximately 3.14159.", ["3.14159"]),
        ("In 2020, the population was 7.8 billion.", ["2020", "7.8"]),
        ("The price is 99.99 dollars.", ["99.99"]),
        ("No numbers here!", []),
    ],
)
def test_pattern(
    text: str,
    values: list[str],
) -> None:
    result = PATTERN_I_DECIMAL_NUMBER_IN_TEXT.findall(text)
    assert result == values


@pytest.mark.parametrize(
    ("text", "sum_value"),
    [
        pytest.param(
            "Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.",  # noqa: RUF001
            "1351.46",
            id="from task",
        ),
        #
        ("No numbers here!", "0"),
        ("The total is 100.", "100"),
        ("Values: 10, 20, and 30.", "60"),
        ("Mixed numbers: 5.5, 2.3, and 7.2.", "15.0"),
        ("Large numbers: 1000000 and 2500000.", "3500000"),
        ("Decimal and integer: 3.14 and 42.", "45.14"),
    ],
    ids=generate_id,
)
def test_sum_profit(
    text: str,
    sum_value: str,
) -> None:
    result = sum_profit(text, generator_numbers)
    expected = Decimal(sum_value)
    assert result == expected
