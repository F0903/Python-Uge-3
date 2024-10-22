from csv_parsing.parser import CsvParser
from csv_parsing.bad_line_mode import BadLineMode
from csv_parsing.error import CsvError
from csv_parsing.validator import CsvTypeValidator
import re

try:
    file = open("csv_test_no_errors.csv")

    parser = CsvParser(file, BadLineMode.WARNING)
    """ validator = CsvTypeValidator(
        {
            # Check types are valid with Regex
            "customer_id": re.compile("\\d+"),
            "name": re.compile(".*"),
            "email": re.compile(".*"),
            "purchase_amount": re.compile(".*"),
        }
    ) """

    for row in parser.parse():
        if row == None:
            break
        print(row)
except CsvError as e:
    print(e.get_printable_message())
