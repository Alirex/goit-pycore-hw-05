import datetime

import pytest

from goit_pycore_hw_05.task_3.constants.log_level import LogLevel
from goit_pycore_hw_05.task_3.models.log_event_info import LogEventInfo
from goit_pycore_hw_05.task_3.services.parse_log_line import LOG_WRONG_FORMAT_ERROR_MSG, parse_log_line


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        (
            "2024-01-22 08:30:01 INFO User logged in successfully.",
            LogEventInfo(
                date=datetime.date(2024, 1, 22),
                time=datetime.time(8, 30, 1),
                level=LogLevel.INFO,
                message="User logged in successfully.",
            ),
        ),
        (
            "2024-01-22 08:45:23 DEBUG Attempting to connect to the database.",
            LogEventInfo(
                date=datetime.date(2024, 1, 22),
                time=datetime.time(8, 45, 23),
                level=LogLevel.DEBUG,
                message="Attempting to connect to the database.",
            ),
        ),
        pytest.param(
            "2024-01-22 08:45:23 debug Attempting to connect to the database.",
            LogEventInfo(
                date=datetime.date(2024, 1, 22),
                time=datetime.time(8, 45, 23),
                level=LogLevel.DEBUG,
                message="Attempting to connect to the database.",
            ),
            id="level in other case",
        ),
        pytest.param(
            "2024-01-22 08:45:23 DEbug Attempting to connect to the database.",
            LogEventInfo(
                date=datetime.date(2024, 1, 22),
                time=datetime.time(8, 45, 23),
                level=LogLevel.DEBUG,
                message="Attempting to connect to the database.",
            ),
            id="level in other case 2",
        ),
    ],
)
def test_parse_log_line(
    line: str,
    expected: LogEventInfo,
) -> None:
    result = parse_log_line(line)
    assert result == expected


@pytest.mark.parametrize(
    "line",
    [
        pytest.param("2024-01-22 INFO User logged in successfully.", id="missing element"),
        pytest.param("2024-01-22 08:30:01 G Attempting to connect to the database.", id="wrong level"),
        pytest.param("2024-51-22 08:30:01 INFO User logged in successfully.", id="wrong date"),
        pytest.param("2024-01-22 24:30:01 INFO User logged in successfully.", id="wrong time"),
    ],
)
def test_parse_log_line_invalid(
    line: str,
) -> None:
    with pytest.raises(ValueError, match=LOG_WRONG_FORMAT_ERROR_MSG):
        parse_log_line(line)
