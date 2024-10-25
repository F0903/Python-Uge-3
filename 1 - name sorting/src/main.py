from utils import remove_duplicates
from sorting import sort_strings_alphabetically, sort_strings_by_length
from stats import get_occurances_of_characters
from plotting.plot import Plot
from names import names
from wordcloud import WordCloud
from plotting.plot import Plot
from stats import (
    get_average_string_length,
    get_median_string_length,
    get_occurances_of_characters,
)


def plot_char_occurances_in_list(list: list[str], list_name: str):
    occurances = get_occurances_of_characters(list, True)
    occurances = dict(
        sorted(occurances.items(), key=lambda item: item[1], reverse=True)
    )

    keys = occurances.keys()
    values = occurances.values()

    plot = (
        Plot()
        .set_xlabel("Characters")
        .set_ylabel("Occurances")
        .set_title(f"Occurances of characters in {list_name}")
    )
    plot.bar_graph(keys, values)


def plot_frequency_word_cloud(word_dict: dict[str, int]):
    cloud = WordCloud()
    cloud = cloud.generate_from_frequencies(word_dict)

    Plot().set_axis("off").imshow(cloud)


def plot_string_length_analysis(strings: list[str], name: str):
    average = get_average_string_length(strings)
    median = get_median_string_length(strings)

    plot = (
        Plot()
        .set_ylabel("Length")
        .set_title(f"String length analysis of {name}")
        .set_color("purple")
    )
    plot.bar_graph(["Average", "Median"], [average, median])


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
    Plot.show_all_plots()
