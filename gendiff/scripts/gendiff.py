from gendiff.gendiff_help import parse
from gendiff.data import read_data

def main():
	args = parse()
	print(read_data(args.first_file))
	print(read_data(args.second_file))


if __name__=='__main__':
	main()