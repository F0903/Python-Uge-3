from utils import remove_duplicates
from sorting import sort_strings_alphabetically, sort_strings_by_length
from stats import get_occurances_of_characters
from plots import (
    plot_char_occurances_in_list,
    plot_frequency_word_cloud,
    plot_string_length_analysis,
    show_all_plots,
)
from names import names

if __name__ == "__main__":
    # Remove duplicates in names
    names = remove_duplicates(names)

    print(f"Length sorting: {sort_strings_by_length(names)}\n")
    print(f"Alphabetical sorting: {sort_strings_alphabetically(names)}\n")
    print(
        f"Occurance of characters in 'names': {get_occurances_of_characters(names, True)}\n"
    )

    plot_char_occurances_in_list(names, "names")
    plot_frequency_word_cloud(get_occurances_of_characters(names, True))
    plot_string_length_analysis(names, "names")
    show_all_plots()
