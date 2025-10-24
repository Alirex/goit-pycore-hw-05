import enum

# Note: enum used for better "CLI help" and ensuring levels.


@enum.unique
class LogLevel(enum.StrEnum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

    def __str__(self) -> str:
        return self.value.upper()
