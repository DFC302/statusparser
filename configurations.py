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
	# Write output to file
	parser.add_argument(
		"--textfile",
		help="Simple text file output.  Output file=statusparser_report.txt.",
		action="store",
	)
	# CSV output
	parser.add_argument(
		"--csvfile",
		help="Save results to CSV output. Output file=statusparser_report.csv.",
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
	parser.add_argument( 
		"--timeout",
		help="Specify number in seconds for URL timeout. Default 3",
		action="store",
		type=float,
	)
	# Write errors to error file
	parser.add_argument(
		"--errorfile",
		help="Write errors to file. By default, errors are not written to file.",
		action="store",
	)
	# Turn off color output
	parser.add_argument(
		"--nocolors",
		help="Print with no color output.",
		action="store_true",
	)
	# Suppress errors
	parser.add_argument(
		"--noerrors",
		help="Silence errors.",
		action="store_true",
	)
	# Parse for only certain statuscodes
	parser.add_argument(
		"-s", "--statuscode",
		help="Print only URL's that return a certain status code.",
		nargs="+",
		type=int,
	)

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args
