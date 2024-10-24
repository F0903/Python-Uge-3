def sort_strings_by_length(strings: list[str]) -> list[str]:
    list = sorted(strings, key=len)
    return list

def sort_strings_alphabetically(strings: list[str]) -> list[str]:
    list = sorted(strings)
    return list