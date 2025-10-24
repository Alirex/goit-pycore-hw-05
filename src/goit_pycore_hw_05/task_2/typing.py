from collections.abc import Generator
from decimal import Decimal
from typing import TypeAlias

T_NUMBER: TypeAlias = Decimal

T_GENERATOR_NUMBERS: TypeAlias = Generator[T_NUMBER]
