import pathlib
from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_3.services.parse_log_line import parse_log_line

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_3.models.log_event_info import T_LOG_EVENTS


def load_logs(file_path: str | pathlib.Path) -> T_LOG_EVENTS:
    """Load logs from a file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    # Note: "file_path" can be a `str` because of "Task requirements".
    file_path = pathlib.Path(file_path)

    # Note: "list comprehension" used for satisfying "Task requirements".
    return [parse_log_line(line) for line in file_path.read_text().splitlines()]
