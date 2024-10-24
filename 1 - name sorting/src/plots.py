import matplotlib.pyplot as plt
from wordcloud import WordCloud
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

    plt.figure()
    plt.bar(keys, values, color="red")
    plt.xlabel("Characters")
    plt.ylabel("Occurances")
    plt.title(f"Occurances of characters in {list_name}")
    plt.tight_layout()


def plot_frequency_word_cloud(word_dict: dict[str, int]):
    cloud = WordCloud()
    cloud = cloud.generate_from_frequencies(word_dict)

    plt.figure()
    plt.imshow(cloud)
    plt.axis("off")
    plt.tight_layout()


def plot_string_length_analysis(strings: list[str], name: str):
    average = get_average_string_length(strings)
    median = get_median_string_length(strings)

    plt.figure()
    plt.bar(["Average", "Median"], [average, median], color="purple")
    plt.ylabel("Length")
    plt.title(f"String length analysis of {name}")
    plt.tight_layout()


def show_all_plots():
    plt.show()
