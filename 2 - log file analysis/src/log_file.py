from enum import Enum
from collections.abc import Iterable
from pathlib import Path


class LogFileErrorType(Enum):
    COULD_NOT_OPEN = 0


class LogFileError(Exception):
    def __init__(self, type: LogFileErrorType, message: str, *args):
        super().__init__(*args)
        self.type = type


class LogFile:
    def __init__(self, path: str):
        self.path = Path(path).absolute()
        self.is_open = False
        pass

    def seek_to_start(self):
        self.file.seek(0)

    def open(self):
        try:
            if self.is_open:
                return
            self.file = open(self.path)
            self.is_open = True
        except OSError as e:
            raise LogFileError(
                LogFileErrorType.COULD_NOT_OPEN,
                f"Could not open '{self.path} for reading!\nFull error: {e.strerror}'",
            )

    def get_line_iter(self) -> Iterable[str]:
        for line in self.file:
            yield line

    def close(self):
        if not self.is_open:
            return
        self.file.close()
        self.is_open = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()
