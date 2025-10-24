from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.constants.command import Command
from goit_pycore_hw_05.task_4.handlers.add_contact import add_contact
from goit_pycore_hw_05.task_4.handlers.change_contact import change_contact
from goit_pycore_hw_05.task_4.handlers.get_contact_phone_by_username import get_contact_phone_by_username
from goit_pycore_hw_05.task_4.handlers.show_all import show_all
from goit_pycore_hw_05.task_4.handlers.show_hello import show_hello

if TYPE_CHECKING:
    from collections.abc import Callable

    from goit_pycore_hw_05.task_4.typing import T_ARGS, T_CONTACTS, T_MESSAGE_FORMATTED


COMMANDS_MAPPING: dict[Command, Callable[[T_ARGS, T_CONTACTS], T_MESSAGE_FORMATTED]] = {
    Command.HELLO: show_hello,
    #
    Command.ADD: add_contact,
    Command.CHANGE: change_contact,
    Command.PHONE: get_contact_phone_by_username,
    Command.ALL: show_all,
}
