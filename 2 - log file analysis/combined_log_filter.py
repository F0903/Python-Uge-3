from log_filter import LogFilter
from collections.abc import Iterable

class CombinedLogFilter(LogFilter):
    def __init__(self, *filters: LogFilter):
        self.filters = filters    

    def is_match(self, string: str) -> bool:
        # Check if any of the filters had a match.
        return any(map(lambda filter: filter.is_match(string), self.filters))