import pathlib  # noqa: TC003
from typing import Annotated

import typer

from goit_pycore_hw_05.task_3.constants.log_level import LogLevel  # noqa: TC001
from goit_pycore_hw_05.task_3.services.count_logs_by_level import count_logs_by_level
from goit_pycore_hw_05.task_3.services.display_log_counts import display_log_counts
from goit_pycore_hw_05.task_3.services.display_log_events_for_level import display_log_events_for_level
from goit_pycore_hw_05.task_3.services.load_logs import load_logs

app = typer.Typer()


@app.command()
def parse_logs(
    file_path: Annotated[pathlib.Path, typer.Argument(help="Path to the log file")],
    log_level_or_none: Annotated[
        LogLevel | None,
        typer.Argument(help="Log level to filter by. If used, extra data will be shown."),
    ] = None,
) -> None:
    logs = load_logs(file_path)

    display_log_counts(count_logs_by_level(logs))

    if log_level_or_none:
        display_log_events_for_level(
            logs=logs,
            log_level=log_level_or_none,
        )
