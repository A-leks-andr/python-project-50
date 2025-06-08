import json
from pathlib import Path

from gendiff.generate import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    with open(get_test_data_path(filename), "r") as file:
        text = json.load(file)
    return text


def test_generate_diff():
    file1 = get_test_data_path("file_1.json")
    file2 = get_test_data_path("file_2.json")
    expec1 = read_file("file_3.json")
    expec2 = read_file("file_4.json")
    print(expec1)
    print(expec2)

    assert generate_diff(file1, file2) == expec1
    assert generate_diff(file2, file1) == expec2
