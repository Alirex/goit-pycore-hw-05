from typing import TYPE_CHECKING, NamedTuple

from pydantic import Field

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_COMMAND


class UserInput(NamedTuple):
    command: T_COMMAND
    args: T_ARGS = Field(
        default_factory=list,
        description="List of arguments for the command.",
    )


def parse_input(user_input: str) -> UserInput:
    _parts = user_input.strip().split()
    command = _parts.pop(0)
    args = _parts
    return UserInput(command=command, args=args)
