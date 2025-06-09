import json
from pathlib import Path

import yaml

from gendiff.generate import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    if Path(filename).suffix == ".json":
        with open(get_test_data_path(filename), "r") as file:
            text = json.load(file)
    elif Path(filename).suffix in (".yaml", "yml"):
        with open(filename, "r") as file:
            text = yaml.load(file, Loader=yaml.SafeLoader)
    return text


def test_generate_diff_json():
    file1 = get_test_data_path("file_1.json")
    file2 = get_test_data_path("file_2.json")
    expec1 = read_file("file_3.json")
    expec2 = read_file("file_4.json")
    actual1 = generate_diff(file1, file2)
    actual2 = generate_diff(file2, file1)
    print(actual1)
    print(actual2)

    assert actual1 == expec1
    assert actual2 == expec2


def test_generate_diff_yaml():
    file1 = get_test_data_path("file_1.yaml")
    file2 = get_test_data_path("file_2.yaml")
    expec1 = read_file("file_3.json")
    expec2 = read_file("file_4.json")
    actual1 = generate_diff(file1, file2)
    actual2 = generate_diff(file2, file1)
    print(actual1)
    print(actual2)

    assert actual1 == expec1
    assert actual2 == expec2
