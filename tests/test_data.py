from pathlib import Path

from gendiff.data import read_data


def get_test_data_path(filename):
    return Path(__file__).parent / "tests" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_read_data():
    file1 = get_test_data_path("file_1.json")
    file2 = get_test_data_path("file_2.json")
    expec1 = read_file("r_data1.txt")
    expec2 = read_file("r_data2.txt")

    assert read_data(file1) == expec1
    assert read_data(file2) == expec2
