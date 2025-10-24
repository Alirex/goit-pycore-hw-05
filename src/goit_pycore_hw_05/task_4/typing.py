from typing import TypeAlias

T_USERNAME: TypeAlias = str
T_PHONE: TypeAlias = str

T_CONTACTS: TypeAlias = dict[T_USERNAME, T_PHONE]

T_MESSAGE_RAW: TypeAlias = str
T_MESSAGE_FORMATTED: TypeAlias = str

T_COMMAND: TypeAlias = str
T_ARGS: TypeAlias = list[str]
