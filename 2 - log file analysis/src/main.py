from log_filter import LogFilter
from log_file import LogFile
from combined_log_filter import CombinedLogFilter
import sys

warning_filter = LogFilter(".*WARNING.*")
error_filter = LogFilter(".*ERROR.*")
warning_error_filter = CombinedLogFilter(warning_filter, error_filter)

args_len = len(sys.argv)

file_output = False

# If the args length is less than 2 then the user has not provided a file path to scan.
if args_len < 2:
    raise Exception("You must provide a log file to filter!")
elif (
    args_len == 3
):  # If the args length is equal to 3 then it is assumed that the 3rd arg is the output file.
    file_output = True
    output_file = open("output.txt", "w")

log_file = LogFile(sys.argv[1])

with log_file:
    output = output_file if file_output else None
    print(
        "----------=[PRINTING WARNINGS AND ERRORS]=----------", file=output
    )  # Only print to file if output file is specified
    combined_iter = warning_error_filter.filter_log_file(log_file)
    for highlight in combined_iter:
        print(highlight, file=output)
    print()
