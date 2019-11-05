#!/usr/bin/env python3

import statusparser_core.colormode
import statusparser_core.nocolor
import sys
from statusparser_core.configurations import options

def main():
	if options().nocolors:
		sp = statusparser_core.nocolor.StatusParserNoColor()
		sp.parser()

	elif not options().nocolors:
		sp = statusparser_core.colormode.StatusParserColorMode()
		sp.parser()

if __name__ == "__main__":
	main()
	sys.exit(0)
