from optparse import OptionParser
from languages import *


def main():
	path, language = parse_command_line()
	counter = get_counter_for_language(language)
	result = counter.get_packages_size(path)
	print_result(result)


def parse_command_line():
	"""Do the command line parsing, returning (the language, base path)"""

	parser = OptionParser(usage="Usage: %prog [options] base_path")
	parser.add_option("-l", "--language", help="Source code language")

	(options, args) = parser.parse_args()
	error_message = check_parse_errors(options, args)

	if error_message != None:
		parser.error(error_message)

	return (args[0], options.language.lower())


def check_parse_errors(options, args):
	"""Do validations on command line options, returning error messages, if any."""

	if not options.language:
		return "language parameter not informed."
	elif not args:
		return "base path not informed."
	else:
		return None


def print_result(result):
	"""Prints to stdout the dictionary of package counts in format
	[package_name][count]"""

	for pack, count in result.items():
		print("{:s}\t{:d}".format(pack, count))

	print("\nAverage:\t{:.2f}".format(calculate_average(result)))


def calculate_average(result):
	"""Calculates the average package size"""

	vals = result.values()
	if len(vals) == 0:
		raise ValueError("Cannot calculate average on empty dictionary.")

	return sum(vals)/len(vals)


if __name__ == '__main__':
	main()