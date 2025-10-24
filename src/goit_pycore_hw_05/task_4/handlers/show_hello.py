from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.utils.format import format_system_message

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_CONTACTS, T_MESSAGE_FORMATTED


# noinspection PyUnusedLocal
def show_hello(
    args: T_ARGS,  # noqa: ARG001
    contacts: T_CONTACTS,  # noqa: ARG001
) -> T_MESSAGE_FORMATTED:
    return format_system_message("How can I help you?")
