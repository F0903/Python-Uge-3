from log_filter import LogFilter
from log_file import LogFile
from combined_log_filter import CombinedLogFilter
import sys

warning_filter = LogFilter(".*WARNING.*")
error_filter = LogFilter(".*ERROR.*")
warning_error_filter = CombinedLogFilter(warning_filter, error_filter)

if len(sys.argv) < 2:
    raise Exception("You must provide a log file to filter!")

log_file = LogFile(sys.argv[1])

with log_file:
    print("----------=[PRINTING WARNINGS]=----------")
    warning_iter = warning_filter.filter_log_file(log_file)
    for warning in warning_iter:
        print(warning)
    print()

    log_file.seek_to_start()

    print("----------=[PRINTING ERRORS]=----------")
    error_iter = error_filter.filter_log_file(log_file)
    for error in error_iter:
        print(error)
    print()

    log_file.seek_to_start()

    print("----------=[PRINTING WARNINGS AND ERRORS]=----------")
    combined_iter = warning_error_filter.filter_log_file(log_file)
    for highlight in combined_iter:
        print(highlight)
    print()