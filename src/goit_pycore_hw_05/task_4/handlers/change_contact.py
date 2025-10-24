from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.constants.command import Command
from goit_pycore_hw_05.task_4.models.message_response import MessageResponse
from goit_pycore_hw_05.task_4.services.validate_phone import validate_phone

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_CONTACTS, T_MESSAGE_FORMATTED


def change_contact(
    args: T_ARGS,
    contacts: T_CONTACTS,
) -> T_MESSAGE_FORMATTED:
    try:
        name, phone = args
    except ValueError:
        return MessageResponse(
            text=f"Invalid arguments. Usage: {Command.CHANGE} [name] [phone]",
            is_error=True,
        ).to_output()

    phone_validation_result = validate_phone(phone)
    if not phone_validation_result.is_valid():
        return phone_validation_result.get_error_message()
    phone = phone_validation_result.get_value()

    if name not in contacts:
        return MessageResponse(
            text=f"Contact with name {name} does not exist.",
            is_error=True,
        ).to_output()

    contacts[name] = phone
    return MessageResponse(
        text="Contact updated.",
    ).to_output()
