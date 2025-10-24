import re
from re import Pattern
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from goit_pycore_hw_03.normalize_phone.typing import T_PHONE_NUMBER_NORMALIZED, T_PHONE_NUMBER_RAW

PATTERN_I_PHONE_I_CHARS_FOR_CLEANUP: Pattern[str] = re.compile(r"[^\d+]")
PATTERN_I_PHONE_I_VALID_NUMBER: Pattern[str] = re.compile(r"^\+(?P<country>\d{2})(?P<operator>\d{3})(?P<number>\d{7})$")
SIZE_I_PHONE__NUMBER_I_OPERATOR_WITH_RELATED: Final[int] = 3 + 7  # Operator + Number
PREFIX_I_INTERNATIONAL_CHAR: Final[str] = "+"
PREFIX_I_UKRAINE_PART: Final[str] = "38"


def normalize_phone(phone_number: T_PHONE_NUMBER_RAW) -> T_PHONE_NUMBER_NORMALIZED:
    """Normalize phone number.

    Focused on the Ukraine area.

    Raises:
        ValueError: if the phone number is invalid and can't be normalized.
    """
    # Remove bad characters
    phone_number_cleaned = PATTERN_I_PHONE_I_CHARS_FOR_CLEANUP.sub("", phone_number)

    # Check and fix if country code is needed.
    if len(phone_number_cleaned) == SIZE_I_PHONE__NUMBER_I_OPERATOR_WITH_RELATED:
        phone_number_cleaned = f"{PREFIX_I_UKRAINE_PART}{phone_number_cleaned}"

    # Add international prefix if needed.
    if not phone_number_cleaned.startswith(PREFIX_I_INTERNATIONAL_CHAR):
        phone_number_cleaned = f"{PREFIX_I_INTERNATIONAL_CHAR}{phone_number_cleaned}"

    # Final validation.
    if not PATTERN_I_PHONE_I_VALID_NUMBER.match(phone_number_cleaned):
        msg = f"Invalid phone number. Source: '{phone_number}'. Normalized: '{phone_number_cleaned}'"
        raise ValueError(msg)

    return phone_number_cleaned
