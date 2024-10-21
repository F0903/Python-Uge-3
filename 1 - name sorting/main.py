from utils import remove_duplicates
from sorting import sort_strings_alphabetically, sort_strings_by_length
from stats import get_occurances_of_characters
from plots import plot_char_occurances_in_list, plot_frequency_word_cloud, plot_string_length_analysis

names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Emily", "Frederik", 
    "Gabriel", "Hannah", "Isabella", "Jacob", "Katherine", "Liam", "Mia", 
    "Nathan", "Olivia", "Peter", "Quinn", "Rebecca", "Samuel", "Theresa", 
    "Ulysses", "Victoria", "William", "Xander", "Yasmine", "Zachary",
    "Amelia", "Aaron", "Sophia", "Noah", "Ava", "James", "Lucas", "Ethan", 
    "Ella", "David", "Elijah", "Aria", "Jackson", "Aiden", "Scarlett", 
    "Sofia", "Matthew", "Logan", "Abigail", "Grace", "Henry", "Isla", 
    "Ryan", "Evelyn", "Oliver", "Sebastian", "Harper", "Caleb", "Chloe", 
    "Julian", "Penelope", "Levi", "Victoria", "Dylan", "Aurora", "Luke", 
    "Hazel", "Isaac", "Samantha", "Theodore", "Lily", "Grayson", "Lillian", 
    "Joshua", "Layla", "Zoe", "Madison", "Owen", "Caroline", "Leo", 
    "Alice", "Mason", "Eleanor", "Wyatt", "Ellie", "Jack", "Nora", "Lucas",
    "Sarah", "Evan", "Luna", "Mila", "Eli", "Sadie", "Landon", "Addison",
    "Jaxon", "Piper", "Lincoln", "Stella", "Connor", "Grace", "Hudson", 
    "Ruby", "Carson", "Sophia", "Asher", "Kinsley", "Christian", "Brielle",
    "Maverick", "Vivian", "Nolan", "Emilia", "Hunter", "Camila", "Adrian", 
    "Archer", "Easton", "Emery", "Maddox", "Faith", "Roman", "Riley"
]

if __name__ == "__main__":
    # Remove duplicates in names
    names = remove_duplicates(names)

    print(f"Length sorting: {sort_strings_by_length(names)}\n")
    print(f"Alphabetical sorting: {sort_strings_alphabetically(names)}\n")
    print(f"Occurance of characters in 'names': {get_occurances_of_characters(names, True)}\n")
    plot_char_occurances_in_list(names, "names")
    plot_frequency_word_cloud(get_occurances_of_characters(names, True))
    plot_string_length_analysis(names, "names")