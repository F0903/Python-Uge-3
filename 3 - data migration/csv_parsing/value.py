from .token import CsvValueToken


class CsvValue:
    def __init__(self, collumn_type: str, token: CsvValueToken) -> None:
        self._collumn_type = collumn_type
        self._token = token

    def get_collumn_type(self) -> str:
        return self._collumn_type

    def get_value(self) -> str:
        return self._token.value

    def debug_get_token(self) -> CsvValueToken:
        return self._token

    def __repr__(self) -> str:
        return f"[{self._collumn_type} = {self.get_value()}]"
