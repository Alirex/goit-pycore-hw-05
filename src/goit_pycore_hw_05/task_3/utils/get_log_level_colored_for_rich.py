from goit_pycore_hw_05.task_3.constants.log_level import LogLevel


def get_log_level_colored_for_rich(level: LogLevel) -> str:
    match level:
        case LogLevel.DEBUG:
            color = "cyan"
        case LogLevel.INFO:
            color = "green"
        case LogLevel.WARNING:
            color = "yellow"
        case LogLevel.ERROR:
            color = "red"
        case _:
            msg = f"Unknown log level: {level}"
            raise ValueError(msg)

    return f"[{color}]{level}[/{color}]"
