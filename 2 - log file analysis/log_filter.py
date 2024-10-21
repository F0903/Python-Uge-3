import re
from collections.abc import Iterable
from log_file import LogFile

class LogFilter:
    def __init__(self, filter_regex: re.Pattern):
        self.pattern = filter_regex

    def is_match(self, string: str) -> bool:
        match = re.match(self.pattern, string)
        return match != None

    def filter_occurances(self, input: Iterable[str]) -> Iterable[str]:
        for line in input:
            if not self.is_match(line):
                continue
            yield line.strip("\r\n") # Remove newline
    
    def filter_log_file(self, log_file: LogFile) -> Iterable[str]:
        line_iter = log_file.get_line_iter()
        match_iter = self.filter_occurances(line_iter)
        return match_iter

    def filter_file(self, file_path: str) -> Iterable[str]:
        log_file = LogFile(file_path)
        with log_file:
            return self.filter_log_file(log_file)