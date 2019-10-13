#!/usr/bin/env python3

import requests
import argparse
import sys
import concurrent.futures
import socket
from colorama import Fore, Style

# Suppress errors if verify is turned off
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def options():
	parser = argparse.ArgumentParser()

	parser.add_argument(
		"-f", "--file",
		help="Specify input file containing list of URLs",
		action="store",
	)

	parser.add_argument(
		"-o", "--out",
		help="Specify output file.",
		action="store",
	)

	parser.add_argument( # Default is 10
		"-t", "--threads",
		help="Specify number of threads.",
		action="store",
		type=int,
	)

	parser.add_argument( # Default is 5
		"--timeout",
		help="Specify number in seconds for URL timeout.",
		action="store",
		type=int,
	)

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args

def write_to_file(url, status_code):
	with open(options().out, "a") as f:
		f.write(f"{status_code}\t{url}\n")

def parser():
	with open(options().file, "r") as f:
		urls = [url.strip("\n").replace("__", "://").replace("_", ".") for url in f]

		if not options().threads:
			threads = 10
		elif options().threads:
			threads = options().threads

		with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
			for _ in executor.map(url_responses, urls):
				pass

def url_responses(url, timeout=5):
	RED = Fore.RED # Error
	GREEN = Fore.GREEN # Success
	YELLOW = Fore.YELLOW # Status codes
	WHITE = Fore.WHITE # Information
	RESET = Style.RESET_ALL # Reset term colors
	
	if url.startswith("http://"):
		url = f"{url}:80"
	elif url.startswith("https://"):
		url = f"{url}:443"

	elif not url.startswith("http://") or not url.startswith("https://"):
		# Assume http, if https, it should redirect
		url = f"http://{url}:80" 

	if options().timeout:
		timeout = options().timeout
	
	try:
		# redirects set to True, verify SSL is False
		response = requests.head(url, allow_redirects=True, verify=False, timeout=timeout)
		status_code = response.status_code
		
		print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")

		if options().out:
			write_to_file(url=url, status_code=str(status_code))

	# Handle all errors encountered
	except requests.ConnectionError:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		# Rather than declare global variables
		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")

	except TypeError:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")

	except socket.gaierror:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")

	except socket.timeout:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")


	except requests.exceptions.ReadTimeout:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")

	except requests.exceptions.TooManyRedirects:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")

	except requests.exceptions.InvalidURL:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")

	except UnicodeError:
		try:
			print(f"{GREEN}{url}\n{WHITE}Status Code: {YELLOW}{status_code}\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code=str(status_code))

		except UnboundLocalError:
			print(f"{RED}{url}\n{WHITE}Status Code: {YELLOW}Undetermined!\n{RESET}")
			pass

			if options().out:
				write_to_file(url=url, status_code="UNK")

	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == "__main__":
	parser()
