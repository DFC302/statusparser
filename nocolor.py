#!/usr/bin/env python3

import requests
import sys
import concurrent.futures
import socket

from configurations import options	
# Suppress errors if verify is turned off
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class StatusParserNoColor():

	def __init__(self):
		self.threads = 20
		self.timeout = 3

	def success(self, url, rurl, port, statuscode):
		with open(options().out, "a") as f:
			f.write(f"URL: {url}\nRedirect: {rurl}:{port}\nStatus Code: {statuscode}\n\n")

	def errors(self, url, rurl, status):
		if options().errorfile:
			with open("Error_report.txt", "a") as ef:
				ef.write(f"URL: {url}\nRedirect: {rurl}\nStatus: {status}\n\n")

		elif not options().errorfile:
			with open(options().out, "a") as ef:
				ef.write(f"URL: {url}\nRedirect: {rurl}\nStatus: {status}\n\n")

	def parser(self):
		with open(options().file, "r") as f:
			# If URL has invalid characterrs in it, replace
			urls = [url.strip("\n").replace("__", "://").replace("_", ".").replace("*.", "http://") + "/" for url in f]

			# Let user choose threads, else use default of 20
			if options().threads:
				threads = options().threads

			else:
				threads = self.threads

			# Start thread pool
			with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
				for _ in executor.map(self.url_responses, urls):
					pass

	def url_responses(self, url):
		# If URl does not start with HTTP://, rewrite URL. Redirects will handle the rest
		# if not url.startswith("http://"):
		# 	url = f"http://{url}"

		# If user specifies a different timeout option, else use default of 3
		if options().timeout:
			timeout = options().timeout
		else:
			timeout = self.timeout

		try:
			# Use a default header
			headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
			# Make request
			response = requests.head(url, allow_redirects=True, verify=False, timeout=timeout, stream=True, headers=headers)
			# Grab URL. This will also grab the redirected URL
			rurl = response.url
			# Grab port number requests made connection on
			port = str(response.raw._connection.sock.getpeername()[1])
			# Grab status code information
			status_code = response.status_code

			# if url was redirected
			if url != rurl:
				if options().statuscode:
					if status_code in options().statuscode:
						print(f"URL: {url}\nRedirect: {rurl}:{port}\nStatus Code: {status_code}\n")
					else:
						pass
				elif not options().statuscode:
					print(f"URL: {url}\nRedirect: {rurl}:{port}\nStatus Code: {status_code}\n")

				if options().out:
					if options().statuscode:
						if status_code in options().statuscode:
							self.success(url=url, rurl=rurl, port=port, statuscode=status_code)
						else:
							pass
					elif not options().statuscode:
						self.success(url=url, rurl=rurl, port=port, statuscode=status_code)

			# If url never redirected
			elif url == url:
				if options().statuscode:
					if status_code in options().statuscode:
						print(f"URL: {url}:{port}\nStatus Code: {status_code}\n")
					else:
						pass
				elif not options().statuscode:
					print(f"URL: {url}:{port}\nStatus Code: {status_code}\n")

				if options().out:
					if options().statuscode:
						if status_code in options().statuscode:
							self.success(url=url, rurl=None, port=port, statuscode=status_code)
						else:
							pass
					elif not options().statuscode:
						self.success(url=url, rurl=None, port=port, statuscode=status_code)

		# Connection Errors
		except requests.ConnectionError:
			if options().noerrors:
				pass
			
			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Connection Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Connection Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Connection Error")

		# Invalid URL Errors
		except socket.gaierror:
			if options().noerrors:
				pass
			
			elif not options().noerrors:
				print(f"URL: {url}\nStatus: GAI Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="GAI Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="GAI Error")

		except requests.exceptions.InvalidURL:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Invalid URL Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Invalid URL Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Invalid URL Error")

		except requests.exceptions.MissingSchema:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Invalid URL Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Invalid URL Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Invalid URL Error")

		# Timeout Errors
		except socket.timeout:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Timeout Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Timeout Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Timeout Error")

		except requests.exceptions.ReadTimeout:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Read Timeout Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Read Timeout Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Read Timeout Error")

		# Redirect Errors
		except requests.exceptions.TooManyRedirects:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Too Many Redirects Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Too Many Redirects Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Too Many Redirects Error")

		# MISC Errors
		except TypeError:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Type Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Type Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Type Error")

		except UnicodeError:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nStatus: Unicode Error\n")
				pass

			if options().out:
				self.errors(url=url, rurl=None, status="Unicode Error")

			elif options().errorfile:
				self.errors(url=url, rurl=None, status="Unicode Error")

		except AttributeError:
			if options().noerrors:
				pass

			elif not options().noerrors:
				print(f"URL: {url}\nRedirect: {rurl}\nStatus Code: Undetermined\nStatus Code Probability: 200\n")
				pass

			if options().out:
				self.errors(url=url, rurl=rurl, status="Undetermined\nStatus Code Probability: 200")

			elif options().errorfile:
				self.errors(url=url, rurl=rurl, status="Undetermined\nStatus Code Probability: 200")

		# If user cancels program
		except KeyboardInterrupt:
			sys.exit(0)

# sp = StatusParserNoColor()
# sp.parser()
