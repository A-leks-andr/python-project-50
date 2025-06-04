import json
import os

def read_data(path_file):
	with open(path_file, 'r') as file:
		strings = dict(sorted(json.load(file).items()))
		return strings