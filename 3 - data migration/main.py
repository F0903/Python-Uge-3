from csv_parsing.parser import CsvParser
from csv_parsing.bad_line_mode import BadLineMode
from csv_parsing.error import CsvError
from csv_parsing.validator import CsvTypeValidator
import re
import sys

args = sys.argv
args_len = len(args)

# We test for 3 instead of 2 because every executable is called with its working dir as the first arg
if args_len < 3:
    raise Exception("You must provide the path to both the input file and output file!")

input_path = args[1]
output_path = args[2]

try:
    with open(input_path, "r") as input, open("error_output.txt", "w") as error, open(
        output_path, "w"
    ) as output:
        parser = CsvParser(input, BadLineMode.WARNING, print_error_to=error)
        validator = CsvTypeValidator(
            {
                # Check types are valid with Regex
                "customer_id": re.compile(r"^\d+$"),
                "name": re.compile(r"^\w+( \w+)*$"),
                "email": re.compile(
                    # Took this one off some website, hope it works as expected lol
                    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                ),
                "purchase_amount": re.compile(r"^\d+\.\d+$"),
            },
            BadLineMode.WARNING,
            print_error_to=error,
        )

        # validate() only returns valid rows
        for row in validator.validate(parser.parse()):
            if row == None:
                break
            # Som jeg har forstået opgaven er der ikke noget specifikt påkrævet fil format
            # til output, så det bliver bare printet ud i mit "ejet" format :)
            print(row, file=output)

except PermissionError as e:
    print(f"Insufficient file permissions!\nFull error: {e}")
except FileNotFoundError as e:
    print("Input file not found!")
