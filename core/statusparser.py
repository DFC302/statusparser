#!/usr/bin/env python3

import core.colormode
import core.nocolor
import sys
from core.configurations import options

def main():
	if options().nocolors:
		sp = nocolor.StatusParserNoColor()
		sp.parser()

	elif not options().nocolors:
		sp = colormode.StatusParserColorMode()
		sp.parser()

if __name__ == "__main__":
	main()
	sys.exit(0)
