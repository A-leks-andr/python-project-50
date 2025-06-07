from gendiff.gendiff_help import parse
from gendiff.generate import generate_diff


def main():
	args = parse()
	print(
		generate_diff(args.first_file, args.second_file)
		)
	
	
if __name__ == '__main__':
	main()