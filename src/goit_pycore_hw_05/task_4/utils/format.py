from typing import TYPE_CHECKING

from rich.markup import escape

from goit_pycore_hw_05.task_4.services.rich_console_wrapper import RichConsoleWrapper

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_MESSAGE_FORMATTED, T_MESSAGE_RAW


def pack_colored_message(message: T_MESSAGE_FORMATTED, color: str) -> T_MESSAGE_FORMATTED:
    with RichConsoleWrapper() as console:
        message = f"[{color}]{escape(message)}[/{color}]"
        console.print(message)
        return console.get_output()


def format_system_message(message: T_MESSAGE_RAW) -> T_MESSAGE_FORMATTED:
    return pack_colored_message(message, "yellow")


def format_prompt_message(message: T_MESSAGE_RAW) -> T_MESSAGE_FORMATTED:
    return pack_colored_message(message, "blue")


def format_response_good_message(message: T_MESSAGE_RAW) -> T_MESSAGE_FORMATTED:
    return pack_colored_message(message, "green")


def format_response_bad_message(message: T_MESSAGE_RAW) -> T_MESSAGE_FORMATTED:
    return pack_colored_message(message, "red")
