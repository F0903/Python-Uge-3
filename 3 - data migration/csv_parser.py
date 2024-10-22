from collections.abc import Iterable
from csv_token import CsvToken, CsvValueToken, CsvTokenType
from typing import cast
from csv_error import CsvError


class CsvParserError(CsvError):
    def __init__(self, message: str, line_num: int) -> None:
        super().__init__(message, line_num)


class CsvHeader:
    def __init__(self, collumn_decls: list[str]) -> None:
        self.collumn_decls = collumn_decls

    def lookup_collumn_type(self, comma_index: int) -> str:
        return self.collumn_decls[comma_index]


class CsvValue:
    def __init__(self, collumn_type: str, value: str) -> None:
        self.collumn_type = collumn_type
        self.value = value

    def get_collumn_type(self) -> str:
        return self.collumn_type

    def get_value(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"[{self.collumn_type} = {self.value}]"


class CsvRow:
    def __init__(self, values: list[CsvValue]) -> None:
        self.values = values

    def get_all_values(self) -> list[CsvValue]:
        return self.values

    def get_value(self, collumn_type: str) -> CsvValue:
        for value in self.values:
            if value.collumn_type != collumn_type:
                continue
            return value

    def __repr__(self) -> str:
        str_buf = ""
        for value in self.values:
            str_buf += f"{value}"
        return str_buf


class CsvParser:
    def __init__(self, input: Iterable[CsvToken]) -> None:
        self.input = input
        self.line_num = 0
        self.current_token = None
        self._parse_header()

    def _parse_header(self):
        self._advance()  # Priming the pump :)
        comma_index = 0
        header_collumn_decls = []
        while True:
            token = self._get_current_token()
            match token.type:
                case CsvTokenType.NEWLINE:
                    self._advance_line()
                    break  # The 'header' is only the first line, so we are done
                case CsvTokenType.COMMA:
                    comma_index += 1
                case CsvTokenType.VALUE:
                    # At this point we know that 'token' is a CsvValueToken
                    value_token = cast(CsvValueToken, token)
                    header_collumn_decls.append(value_token.value)
            self._advance()

        self.header = CsvHeader(header_collumn_decls)

    def _get_current_token(self) -> CsvToken:
        return self.current_token

    def _get_previous_token(self) -> CsvToken:
        return self.previous_token

    def _advance(self):
        self.previous_token = self.current_token
        self.current_token = next(self.input)

    def _advance_line(self):
        self._advance()
        self.line_num += 1

    def parse(self) -> Iterable[CsvRow | None]:
        # We have already 'primed the pump' in _parse_header() so no need to here

        row_values = []
        comma_index = 0
        while True:
            token = self._get_current_token()
            match token.type:
                case CsvTokenType.NEWLINE:
                    row = CsvRow(row_values.copy())

                    row_values.clear()
                    comma_index = 0

                    self._advance_line()
                    yield row
                case CsvTokenType.COMMA:
                    comma_index += 1
                    self._advance()
                case CsvTokenType.VALUE:
                    # At this point we know that 'token' is a CsvValueToken
                    value_token = cast(CsvValueToken, token)

                    try:
                        collumn_type = self.header.lookup_collumn_type(comma_index)
                    except IndexError:
                        raise CsvParserError(
                            "Could not get collumn type, too many commas!",
                            self._get_previous_token(),  # Pass the previous token (which is assumed to be the culprit comma)
                        )
                    value = CsvValue(collumn_type, value_token.value)
                    row_values.append(value)
                    self._advance()
                case CsvTokenType.END_OF_FILE:
                    if len(row_values) != 0:
                        row = CsvRow(row_values.copy())
                        row_values.clear()  # Clearing this will make this yield None on next iter.
                        yield row
                    yield None
