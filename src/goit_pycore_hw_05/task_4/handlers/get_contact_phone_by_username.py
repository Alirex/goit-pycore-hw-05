from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.constants.command import Command
from goit_pycore_hw_05.task_4.models.message_response import MessageResponse

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_CONTACTS, T_MESSAGE_FORMATTED


def get_contact_phone_by_username(
    args: T_ARGS,
    contacts: T_CONTACTS,
) -> T_MESSAGE_FORMATTED:
    try:
        name = args[0]
    except ValueError:
        return MessageResponse(
            text=f"Invalid arguments. Usage: {Command.PHONE} [name]",
            is_error=True,
        ).to_output()

    if name not in contacts:
        return MessageResponse(
            text=f"Contact with name {name} does not exist.",
        ).to_output()

    return MessageResponse(
        text=contacts[name],
    ).to_output()
