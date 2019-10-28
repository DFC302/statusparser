# Changelog
**All notable changes to this project will be recorded here**

# Version 2.2.1
**(Oct 27 2019)**

# Changes
* Errors can now be written a file named after user, in any directory user has access too. (rather than a program generated name and default directory.).
* New option, --textfile. Save output into a simple text file report.
* New option, --csvfile. Save output into a csv file report.

# Version 2.1.1
**(Oct 21 2019)**

# Bug Fixes
* Added support for list of domains that have invalid HTTP scheme. (If url does not start with http://, statusparser will now add it to begining of url. Since redirects are on, if url uses https, it will automatically redirect)

# Version 2.1.0
**(Oct 19 2019)**

# Changes
* Ignore comments in file containing list of URLs
* Removed appened "/" to end of url. Was causing some issues.
* Removed appended port to url. Port now has its own line when printing results.
* Removed appended port to url when writing to file. Port now has its own line when writing to results.
* Added IP of URL to each report.
* IP will also be written to outfile.


# Version 2.0.0
**(Oct 17 2019)**

# Changes
* Better handling of HTTPS
* Automatic URL and port detection -- if url uses http or https
* Write errors to separate file
* Better error reporting -- More descriptive errors
* Option for nocolors
* Suppress errors when running
* Only print certain status codes (can request multiple status codes at the same time.)

# Future Changes
* Ability to set timeout for connect and read, rather than one set timeout for both
* Print descriptive definition of status codes
* Handle URL invalid schemes better
* Possibly the ability to send X number of requests at a time, wait N number of seconds, send X number again, etc.

# Version 1.0

# Notes
**Updates to this project will be coming in the next couple weeks.** 

# Bug fixes
* None

# Changes
* None

# Future Changes
* Check ports other than 80 and 443
* Better error handling and response quality
* More CLI options 
