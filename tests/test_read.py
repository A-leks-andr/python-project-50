import json
from pathlib import Path

import yaml

from gendiff.data import read_data


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


def test_read_data_json():
    file1 = get_test_data_path("file_1.json")
    file2 = get_test_data_path("file_2.json")
    expec1 = read_file("file_1.json")
    expec2 = read_file("file_2.json")

    assert read_data(file1) == expec1
    assert read_data(file2) == expec2


def test_read_data_yaml():
    file1 = get_test_data_path("file_1.yaml")
    file2 = get_test_data_path("file_2.yaml")
    expec1 = read_file("file_1.json")
    expec2 = read_file("file_2.json")

    assert read_data(file1) == expec1
    assert read_data(file2) == expec2
