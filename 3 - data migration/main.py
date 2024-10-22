from csv_lexer import CsvLexer
from csv_parser import CsvParser
from csv_error import CsvError

try:
    file = open("csv_test_no_errors.csv")

    lexer = CsvLexer(file)
    parser = CsvParser(lexer.lex())

    for row in parser.parse():
        if row == None:
            break
        print(row)
except CsvError as e:
    print(e.get_printable_message())
