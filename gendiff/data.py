import json
from pathlib import Path

import yaml


def read_data(path_file):
    if Path(path_file).suffix == ".json":
        with open(path_file, "r") as file:
            strings = json.load(file)
    elif Path(path_file).suffix in (".yaml", ".yml"):
        with open(path_file, "r") as file:
            strings = yaml.load(file, Loader=yaml.SafeLoader)
    return strings
