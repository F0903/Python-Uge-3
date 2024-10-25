from collections.abc import Iterable
from .token import CsvTokenType, CsvToken, CsvValueToken


class CsvLexer:
    def __init__(self, input: Iterable[str]) -> None:
        self.input = input
        self.line_num = 0
        self.line = ""
        self.index = 0
        self.stop_requested = False

    def _advance_line(self):
        try:
            self.line = next(self.input)
        except StopIteration:
            # If we somehow get to this point, then this will make the iter stop gracefully.
            self.stop_requested = True

        self.line_num += 1
        self.index = 0

    def _advance_char(self):
        self.index += 1

    def _get_current_char(self) -> str | None:
        # Return the current char if we are within bounds, otherwise return None
        return self.line[self.index] if len(self.line) > self.index else None

    def _create_value_token(self) -> CsvValueToken:
        start_index = self.index
        str_buf = ""
        while True:
            char = self._get_current_char()

            # Don't handle these cases here.
            if char == "," or char == "\n" or char == None:
                break

            str_buf += char
            self._advance_char()

        return CsvValueToken(str_buf, self.line_num, start_index + 1)

    def lex(self) -> Iterable[CsvToken]:
        self._advance_line()  # Priming the pump :)
        while True:
            if self.stop_requested:
                yield CsvToken(CsvTokenType.END_OF_FILE, self.line_num, self.index)

            char = self._get_current_char()
            match char:
                case ",":
                    self._advance_char()
                    yield CsvToken(CsvTokenType.COMMA, self.line_num, self.index)
                case "\n":
                    self._advance_line()
                    yield CsvToken(CsvTokenType.NEWLINE, self.line_num, self.index)
                case None:
                    # We use an EOF token because it's simpler than handling the StopIteration exception in my opinion.
                    yield CsvToken(CsvTokenType.END_OF_FILE, self.line_num, self.index)
                case _:
                    yield self._create_value_token()
