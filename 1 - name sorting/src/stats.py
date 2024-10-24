import collections
from utils import char_range
from statistics import mean, median


def get_occurance_in_string(string: str, char: str) -> int:
    count = 0
    for ch in string:
        if ch.capitalize() != char.capitalize():
            continue
        count += 1
    return count


def get_occurance_in_string_list(strings: list[str], char: str) -> int:
    occurances = collections.defaultdict()
    for string in strings:
        count = get_occurance_in_string(string, char)
        occurances[string] = count

    occurance_sum = sum(occurances.values())
    return occurance_sum


def get_occurances_of_characters(
    string: list[str], ignore_no_occurances=False
) -> dict[str, int]:
    occurances = collections.defaultdict()
    for char in char_range("A", "Z"):
        count = get_occurance_in_string_list(string, char)
        if count == 0 and ignore_no_occurances:
            continue
        occurances[char] = count
    return occurances


def get_average_string_length(strings: list[str]) -> int:
    average = mean(map(len, strings))
    return average


def get_median_string_length(strings: list[str]) -> int:
    med = median(map(len, strings))
    return med
