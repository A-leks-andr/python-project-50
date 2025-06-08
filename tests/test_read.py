import json
from pathlib import Path

from gendiff.data import read_data


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    with open(get_test_data_path(filename), "r") as file:
        text = json.load(file)
    return text


def test_read_data():
    file1 = get_test_data_path("file_1.json")
    file2 = get_test_data_path("file_2.json")
    expec1 = read_file("file_1.json")
    expec2 = read_file("file_2.json")

    assert read_data(file1) == expec1
    assert read_data(file2) == expec2
