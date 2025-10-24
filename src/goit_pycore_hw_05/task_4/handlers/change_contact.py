from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.constants.command import Command
from goit_pycore_hw_05.task_4.models.message_response import MessageResponse
from goit_pycore_hw_05.task_4.services.input_error import input_error
from goit_pycore_hw_05.task_4.services.validate_phone import validate_phone

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_CONTACTS, T_MESSAGE_FORMATTED


@input_error
def change_contact(
    args: T_ARGS,
    contacts: T_CONTACTS,
) -> T_MESSAGE_FORMATTED:
    try:
        name, phone = args
    except ValueError as exc:
        msg = f"Invalid arguments. Usage: {Command.CHANGE} [name] [phone]"
        raise ValueError(msg) from exc

    phone_validation_result = validate_phone(phone)
    if not phone_validation_result.is_valid():
        raise ValueError(phone_validation_result.get_error_message())

    phone = phone_validation_result.get_value()

    if name not in contacts:
        msg = f"Contact with name {name} does not exist."
        raise IndexError(msg)

    contacts[name] = phone
    return MessageResponse(
        text="Contact updated.",
    ).to_output()
