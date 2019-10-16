#!/usr/bin/env python3

import requests
import argparse
import sys
import concurrent.futures
import socket
from colorama import Fore, Style

from configurations import options

# Suppress errors from SSL verification
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class StatusParser():

	# Colors for color output
	RED = Fore.RED # Error
	GREEN = Fore.GREEN # Success
	YELLOW = Fore.YELLOW # Status codes
	CYAN = Fore.CYAN # Redirected URLS
	MAG = Fore.MAGENTA # Port numbers
	WHITE = Fore.WHITE # Information
	RESET = Style.RESET_ALL # Reset term colors

	HTTP_STATUS_CODES = {
		200:"OK",
		301:"Moved",
		400:"Bad Request",
		401:"Unauthorized",
		403:"Forbidden",
		404:"Not Found",
		410:"Gone",
		500:"Internal Server Error",
		503:"Service Unavailable"
	}

	def __init__(self):
		self.threads = 20
		self.timeout = 2

	def response_statement(self, url, rurl, port, status_code):
		if options().nocolor:
			if url != rurl:
				print(f"URL: {url}\nRedirected URL: {rurl}:{port}\nStatus Code: {status_code}\n")

			elif url == rurl:
				print(f"URL: {url}\nStatus Code: {status_code}\n")
		
		elif not options().nocolor:
			if url != rurl:
				print(f"{self.WHITE}URL: {self.GREEN}{url}\n{self.WHITE}Redirected URL: {self.CYAN}{rurl}:{self.MAG}{port}\n{self.WHITE}Status Code: {self.YELLOW}{status_code}{self.RESET}\n")

			else:
				print(f"{self.WHITE}URL: {self.GREEN}{url}\n{self.WHITE}Status Code: {self.YELLOW}{status_code}{self.RESET}\n")

	def response_error(self, url, error):
		if options().nocolor:
			print(f"URL: {url}\nStatus Code: Undetermined!\n")

		elif not options().nocolor:
			print(f"{self.WHITE}URL: {self.RED}{url}\n{self.WHITE}Status Code: {self.YELLOW}Undetermined!{self.RESET}\n")

	# Thread pool execution\n
	def parser(self):
		with open(options().file, "r") as f:
			# If these characters are present in the url, replace
			urls = [url.strip("\n").replace("__", "://").replace("_", ".").replace("*.", "") + "/" for url in f]
			# If no option for threads is chosen, choose default
			if not options().threads:
				threads = 20
			# Specified threads
			elif options().threads:
				threads = options().threads
			# Start threads
			with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
				for _ in executor.map(self.url_responses, urls):
					pass

	def url_responses(self, url):
		
		if options().timeout:
			timeout = options().timeout
		else:
			timeout = self.timeout		
		try:
			# Better responses with a firefox user-agent
			headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
			# Make request
			response = requests.head(url, allow_redirects=True, verify=False, timeout=timeout, stream=True, headers=headers)
			# Grab the redirected URL, if URL was not redirected, it will be the original URL from the file.
			rurl = response.url
			# IF url is redirected, grab the port number that was used to make a connection
			port = str(response.raw._connection.sock.getpeername()[1])
			# Grab status code
			status_code = response.status_code
			# Print response of request
			self.response_statement(url=url, rurl=rurl, port=port, status_code=status_code)

		# Handle all errors encountered
		except Exception:
			pass

		except UnicodeError:
			pass

		except socket.gaierror:
			pass

		except socket.timeout:
			pass

		except KeyboardInterrupt:
			sys.exit(0)

SP = StatusParser()
SP.parser()
