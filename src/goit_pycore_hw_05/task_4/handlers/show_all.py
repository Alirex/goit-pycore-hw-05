from typing import TYPE_CHECKING

from rich.table import Table

from goit_pycore_hw_03.normalize_phone import PATTERN_I_PHONE_I_VALID_NUMBER
from goit_pycore_hw_05.task_4.services.rich_console_wrapper import RichConsoleWrapper
from goit_pycore_hw_05.task_4.utils.format import format_system_message

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_CONTACTS, T_MESSAGE_FORMATTED


# noinspection PyUnusedLocal
def show_all(
    args: T_ARGS,  # noqa: ARG001
    contacts: T_CONTACTS,
) -> T_MESSAGE_FORMATTED:
    if not contacts:
        return format_system_message("No contacts found.")

    with RichConsoleWrapper() as console:
        table = Table()
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Username")
        table.add_column("Phone")
        for index, value in enumerate(sorted(contacts.items()), start=1):
            username, phone = value

            phone_by_regex = PATTERN_I_PHONE_I_VALID_NUMBER.match(phone)

            if not phone_by_regex:
                msg = f"Invalid phone number: '{phone}'"
                raise ValueError(msg)

            formatted_phone = (
                f"+{phone_by_regex.group('country')}"
                f"[blue]{phone_by_regex.group('operator')}[/blue]"
                f"{phone_by_regex.group('number')}"
            )

            table.add_row(str(index), username, formatted_phone)

        console.print(table)

        return console.get_output()
