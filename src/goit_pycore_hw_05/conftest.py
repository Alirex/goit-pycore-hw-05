import pathlib
from typing import Final

import pytest

TASK_PREFIX: Final[str] = "task_"


def pytest_configure(config: pytest.Config) -> None:
    # Register new markers:
    #   https://docs.pytest.org/en/stable/how-to/mark.html#registering-marks

    config.addinivalue_line(
        "markers",
        "task(id:int): mark test as belonging to a specific task",
    )


# noinspection PyUnusedLocal
def pytest_collection_modifyitems(
    config: pytest.Config,  # noqa: ARG001
    items: list[pytest.Item],
) -> None:
    # Hook:
    #   https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_collection_modifyitems

    # Markers:
    #   https://docs.pytest.org/en/stable/example/markers.html

    # Add markers for tasks tests

    package_root = pathlib.Path(__file__).parent.resolve()

    for item in items:
        try:
            rel_path = pathlib.Path(item.fspath).relative_to(package_root)
        except ValueError:
            continue

        folder_name = rel_path.parts[0]

        if not folder_name.startswith(TASK_PREFIX):
            continue

        task_name = int(folder_name.removeprefix(TASK_PREFIX))

        item.add_marker(pytest.mark.task(id=task_name))
