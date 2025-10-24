from typing import TYPE_CHECKING

from pydantic import BaseModel

from goit_pycore_hw_05.task_4.utils.format import format_response_bad_message, format_response_good_message

if TYPE_CHECKING:
    from goit_pycore_hw_05.task_4.typing import T_MESSAGE_FORMATTED


class MessageResponse(BaseModel):
    text: str
    is_error: bool = False

    def to_output(self) -> T_MESSAGE_FORMATTED:
        if self.is_error:
            return format_response_bad_message(self.text)
        return format_response_good_message(self.text)
