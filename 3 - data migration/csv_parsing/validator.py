import re
from collections.abc import Iterable
from .row import CsvRow
from .value import CsvValue
from .error import CsvError
from .token import CsvToken


class CsvValidatorError(CsvError):
    def __init__(self, message: str, token: CsvToken) -> None:
        super().__init__(message, token)


class CsvTypeValidator:
    def __init__(self, type_pattern_map: dict[str, re.Pattern]) -> None:
        self.type_pattern_map = type_pattern_map

    def _check_value(self, value: CsvValue) -> bool:
        value_type = value.get_collumn_type()
        try:
            pattern = self.type_pattern_map[value_type]
            value_str = value.get_value()

            if not pattern.match(value_str):
                raise CsvValidatorError(
                    f"Wrong type format! Value was '{value.get_value()}' expected regex format is '{pattern.pattern}'",
                    value.debug_get_token(),
                )

            return True
        except KeyError:
            raise CsvValidatorError(
                f"Unknown collumn type! '{value_type}'", value.debug_get_token()
            )

    def validate_row(self, row: CsvRow | None) -> CsvRow | None:
        if row == None:
            return None

        values = row.get_all_values()
        # Make sure ALL values pass the tests.
        if all(map(self._check_value, values)):
            return row

    def validate_iter(self, rows: Iterable[CsvRow | None]) -> Iterable[CsvRow | None]:
        return map(self.validate_row, rows)
