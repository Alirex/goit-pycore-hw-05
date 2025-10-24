from collections import Counter
from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_3.constants.log_level import LogLevel

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_3.models.log_event_info import T_LOG_EVENTS

type T_LOGS_COUNT = dict[LogLevel, int]


def count_logs_by_level(logs: T_LOG_EVENTS) -> T_LOGS_COUNT:
    return Counter(log["level"] for log in logs)
