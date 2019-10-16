#!/usr/bin/env python3

import argparse
import sys

def options():
	parser = argparse.ArgumentParser()

	# File containing list of URLs
	parser.add_argument(
		"-f", "--file",
		help="Specify input file containing list of URLs",
		action="store",
	)
	# Specify number of threads to use
	# Default is 20
	parser.add_argument(
		"-t", "--threads",
		help="Specify number of threads.",
		action="store",
		type=int,
	)
	# Specfify timeout for requests
	parser.add_argument( # Default is 5
		"--timeout",
		help="Specify number in seconds for URL timeout.",
		action="store",
		type=float,
	)
	# Parse for only certain statuscodes
	# parser.add_argument(
	# 	"-r", "--response",
	# 	help="Print only URL's that return a certain status code.",
	# 	nargs="+",
	# 	type=int,
	# )
	# Turn off color output
	parser.add_argument(
		"--nocolor",
		help="Print with no color output.",
		action="store_true",
	)
	# Suppress errors
	# parser.add_argument(
	# 	"--noerrors",
	# 	help="Silence errors.",
	# 	action="store_true",
	# )
	# Print decription of status code
	# parser.add_argument(
	# 	"-d", "--description",
	# 	help="Print descriptions of http response codes.",
	# 	action="store_true",
	# )

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args