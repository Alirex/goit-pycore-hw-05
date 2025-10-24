from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.constants.command import Command
from goit_pycore_hw_05.task_4.models.message_response import MessageResponse
from goit_pycore_hw_05.task_4.services.input_error import input_error

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_CONTACTS, T_MESSAGE_FORMATTED


@input_error
def get_contact_phone_by_username(
    args: T_ARGS,
    contacts: T_CONTACTS,
) -> T_MESSAGE_FORMATTED:
    try:
        name = args[0]
    except IndexError as exc:
        msg = f"Invalid arguments. Usage: {Command.PHONE} [name]"
        raise ValueError(msg) from exc

    if name not in contacts:
        msg = f"Contact with name {name} does not exist."
        raise KeyError(msg)

    return MessageResponse(
        text=contacts[name],
    ).to_output()
