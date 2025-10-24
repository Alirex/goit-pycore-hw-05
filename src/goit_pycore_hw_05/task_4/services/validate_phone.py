from typing import TYPE_CHECKING

from pydantic import BaseModel

from goit_pycore_hw_03.normalize_phone import normalize_phone
from goit_pycore_hw_05.task_4.utils.format import format_response_bad_message

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_MESSAGE_FORMATTED


class PhoneValue(BaseModel):
    value: str


class ErrorMessage(BaseModel):
    message: str


class PhoneValidationResult(BaseModel):
    data: PhoneValue | ErrorMessage

    def is_valid(self) -> bool:
        return isinstance(self.data, PhoneValue)

    def get_value(self) -> str:
        if isinstance(self.data, PhoneValue):
            return self.data.value

        msg = "Wrong usage."
        raise ValueError(msg)

    def get_error_message(self) -> T_MESSAGE_FORMATTED:
        if isinstance(self.data, ErrorMessage):
            return self.data.message

        msg = "Wrong usage."
        raise ValueError(msg)


def validate_phone(phone: str) -> PhoneValidationResult:
    try:
        value = normalize_phone(phone)
    except ValueError as exc:
        return PhoneValidationResult(data=ErrorMessage(message=format_response_bad_message(str(exc))))

    return PhoneValidationResult(data=PhoneValue(value=value))
