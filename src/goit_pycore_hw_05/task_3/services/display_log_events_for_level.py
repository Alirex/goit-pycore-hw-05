from typing import TYPE_CHECKING

import rich

from goit_pycore_hw_05.task_3.services.filter_logs_by_level import filter_logs_by_level
from goit_pycore_hw_05.task_3.utils.get_log_level_colored_for_rich import get_log_level_colored_for_rich

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_3.constants.log_level import LogLevel
    from goit_pycore_hw_05.task_3.models.log_event_info import T_LOG_EVENTS, LogEventInfo


def display_log_events_for_level(logs: T_LOG_EVENTS, log_level: LogLevel) -> None:
    logs_filtered = filter_logs_by_level(logs, log_level)

    console = rich.console.Console()

    msg = f"Деталі логів для рівня '{get_log_level_colored_for_rich(log_level)}':"

    console.print(msg)

    for event in logs_filtered:
        console.print(build_string_for_log_event_simple(event))


def build_string_for_log_event_simple(event: LogEventInfo) -> str:
    return f"{event['date'].isoformat()} {event['time'].isoformat()} - {event['message']}"
