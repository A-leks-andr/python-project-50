from gendiff.data import read_data
from gendiff.search_of_the_diff import search_diff


def generate_diff(first_file, second_file):
    data_1 = read_data(first_file)
    data_2 = read_data(second_file)
    return search_diff(data_1, data_2)
