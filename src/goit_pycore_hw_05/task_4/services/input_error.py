import functools
from typing import TYPE_CHECKING

from goit_pycore_hw_05.task_4.models.message_response import MessageResponse

if TYPE_CHECKING:
    from collections.abc import Callable

    from goit_pycore_hw_05.task_4.typing import T_MESSAGE_FORMATTED


def input_error[**Parameters](
    func: Callable[Parameters, T_MESSAGE_FORMATTED],
) -> Callable[Parameters, T_MESSAGE_FORMATTED]:
    @functools.wraps(func)
    def inner(*args: Parameters.args, **kwargs: Parameters.kwargs) -> T_MESSAGE_FORMATTED:
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as exc:
            # Note: messages of the errors are created at the place where they are raised.
            #   Because different errors are raised in different places.
            #   But "task" requires using only these exceptions.

            # TODO: (?) use more custom exceptions for better error handling.
            return MessageResponse(
                text=str(exc),
                is_error=True,
            ).to_output()

    return inner
