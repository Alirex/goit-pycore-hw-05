import datetime
from typing import TYPE_CHECKING, Final

from goit_pycore_hw_05.task_3.constants.log_level import LogLevel
from goit_pycore_hw_05.task_3.models.log_event_info import LogEventInfo

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_3.typing import T_LOG_LINE

LOG_LINE_BLOCKS_AMOUNT: Final[int] = 4
LOG_WRONG_FORMAT_ERROR_MSG: Final[str] = "Incorrect log line format"


def parse_log_line(line: T_LOG_LINE) -> LogEventInfo:
    """Parse a single log line.

    Raises:
        ValueError: If the line is not in the expected format.
    """
    split_line = line.strip().split(" ", LOG_LINE_BLOCKS_AMOUNT - 1)
    if len(split_line) != LOG_LINE_BLOCKS_AMOUNT:
        msg = LOG_WRONG_FORMAT_ERROR_MSG
        raise ValueError(msg)

    date, time, level, message = split_line

    try:
        return LogEventInfo(
            date=datetime.date.fromisoformat(date),
            time=datetime.time.fromisoformat(time),
            level=LogLevel(level.lower()),
            message=message,
        )
    except ValueError as exc:
        msg = LOG_WRONG_FORMAT_ERROR_MSG
        raise ValueError(msg) from exc
