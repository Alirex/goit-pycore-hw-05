from typing import TYPE_CHECKING

from rich.console import Console
from rich.table import Table

from goit_pycore_hw_05.task_3.utils.get_log_level_colored_for_rich import get_log_level_colored_for_rich

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_3.services.count_logs_by_level import T_LOGS_COUNT


def display_log_counts(counts: T_LOGS_COUNT) -> None:
    console = Console()
    table = Table()
    table.add_column("Рівень логування", justify="left")
    table.add_column("Кількість", justify="left")

    for level, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        table.add_row(get_log_level_colored_for_rich(level), str(count))

    console.print(table)
