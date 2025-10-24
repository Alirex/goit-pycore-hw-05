import io
from typing import TYPE_CHECKING, Any, Self

import rich.console
from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from types import TracebackType


class RichConsoleWrapper(BaseModel):
    console: rich.console.Console = Field(
        default_factory=lambda: rich.console.Console(
            record=True,
            force_terminal=True,
            file=io.StringIO(),
        ),
    )

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    def __enter__(self) -> Self:
        return self

    def print(
        self,
        data: Any,  # noqa: ANN401
        /,
    ) -> None:
        self.console.print(data)

    def get_output(self) -> str:
        return self.console.export_text(styles=True)

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        return None
