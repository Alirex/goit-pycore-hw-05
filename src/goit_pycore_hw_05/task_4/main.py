from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.constants.command import Command
from goit_pycore_hw_05.task_4.handlers.main import COMMANDS_MAPPING
from goit_pycore_hw_05.task_4.services.parse_input import parse_input
from goit_pycore_hw_05.task_4.utils.format import (
    format_prompt_message,
    format_response_bad_message,
    format_system_message,
)

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_CONTACTS


def main() -> None:
    contacts: T_CONTACTS = {}

    # TODO: Rework when restriction "Callable[..., str]" will be removed.
    # TODO: Add help message.
    # TODO: Add `remove` command.

    print(format_system_message("Welcome to the assistant bot!"))
    while True:
        user_input = input(format_prompt_message("Enter a command:"))

        user_input_obj = parse_input(user_input)
        try:
            command = Command(user_input_obj.command)
        except ValueError:
            print(format_response_bad_message("Invalid command."))
            continue

        args = user_input_obj.args

        if command in {Command.CLOSE, Command.EXIT}:
            print(format_system_message("Good bye!"))
            break

        command_func = COMMANDS_MAPPING.get(command)
        if command_func is None:
            print(format_response_bad_message("Invalid command."))
            continue

        print(command_func(args, contacts))


if __name__ == "__main__":
    main()
