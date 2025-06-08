import json

from gendiff.gendiff_help import parse
from gendiff.generate import generate_diff


def main():
    args = parse()
    result = generate_diff(args.first_file, args.second_file)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
