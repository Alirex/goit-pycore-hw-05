from typing import TYPE_CHECKING, TypeAlias, TypedDict

if TYPE_CHECKING:
    import datetime

    from goit_pycore_hw_05.task_3.constants.log_level import LogLevel

# TODO: Rework to pydantic BaseModel

# Note: Used TypedDict because `task` require "dict" type.


class LogEventInfo(TypedDict):
    date: datetime.date
    time: datetime.time

    level: LogLevel

    message: str


T_LOG_EVENTS: TypeAlias = list[LogEventInfo]
