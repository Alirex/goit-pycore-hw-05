import enum


@enum.unique
class Command(enum.StrEnum):
    HELLO = "hello"

    ADD = "add"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"

    CLOSE = "close"
    EXIT = "exit"
