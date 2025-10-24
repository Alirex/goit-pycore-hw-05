from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_3.constants.log_level import LogLevel

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_3.models.log_event_info import T_LOG_EVENTS


def filter_logs_by_level(logs: T_LOG_EVENTS, level: str | LogLevel) -> T_LOG_EVENTS:
    level = LogLevel(level)

    return list(filter(lambda log: log["level"] == level, logs))
