<p align="center">
  <img width="850" height="300" src="https://github.com/DFC302/statusparser/blob/master/images/logo.png">
</p>

# StatusParser
[![BuildStatus](https://travis-ci.org/DFC302/statusparser.svg?branch=master)](https://travis-ci.org/DFC302/statusparser) \
Retrieve the status codes from a list of URLs \
[![Follow on Twitter](https://img.shields.io/twitter/follow/Vail__.svg?logo=twitter)](https://twitter.com/Vail__)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) \
**Check changelog.md for all updates to project**

# Installation:
git clone https://github.com/DFC302/statusparser.git \
python3 setup.py install (may need sudo)

**OR**

git clone https://github.com/DFC302/statusparser.git \
cd statusparser/ \
sudo chmod 755 statusparser

# Requirements:
[![Python3](https://img.shields.io/badge/Made%20with-Python3-1f425f.svg)](https://shields.io/)

**Modules** \
colorama \
argparse \
concurrent.futures \
sys \
socket \
requests.packages.urllib3.exceptions - InsecureRequestWarning

# Usage:
```
usage: statusparser [-h] [-f FILE] [--textfile TEXTFILE] [--csvfile CSVFILE]
                    [-t THREADS] [--timeout TIMEOUT] [--errorfile ERRORFILE]
                    [--nocolors] [--noerrors] [-s STATUSCODE [STATUSCODE ...]]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Specify input file containing list of URLs
  --textfile TEXTFILE   Write results to simple text file output.
  --csvfile CSVFILE     Write results to CSV output.
  -t THREADS, --threads THREADS
                        Specify number of threads.
  --timeout TIMEOUT     Specify number in seconds for URL timeout. Default 3
  --errorfile ERRORFILE
                        Write errors to file. By default, errors are not
                        written to file.
  --nocolors            Print with no color output.
  --noerrors            Silence errors.
  -s STATUSCODE [STATUSCODE ...], --statuscode STATUSCODE [STATUSCODE ...]
                        Print only URL's that return a certain status code.

```
# Example Usage:

**File containing URLs are better off having proper scheme -- http:// or https:// \
However, if they do not, statusparser will add http:// to the domain in question. If the domain uses https, a redirect will catch it.**

**Basic usage** \
Usage: python3 statusparser -f [List of URLs file]

**Write to file** \
Usage: python3 statusparser -f [List of URLs file] --csvfile [Write to file] \
Usage: python3 statusparser -f [List of URLs file] --textfile [Write to file] \
Note: Basic redirection can also be used instead to keep colors in file ">>". WARNING: Doing this, will cause no output to print to screen while statusparser runs.

**Using threads** \
Usage: python3 statusparser -f [List of URLs file] -t [number of threads #default 20]

**Specify timeout** \
Note: timeout is applied to read and connect timeouts \
Note: Lowering timeout may result in connection errors (false status return) \
Usage: python3 statusparser -f [List of URLs file] --timeout [number #converted to a floating integer]

**Send errors to a error file** \
Note: Errors will still be printed to terminal screen, unless option --noerrors is used. \
Usage: python3 statusparser -f [List of URLs file] --errorfile

**No color mode** \
Note: Run statusparser with no colors \
Usage: python3 statusparser -f [List of URLs file] --nocolors

**No error mode** \
Note: Suppress all errors \
Note: If you want errors written to a file you will need to use --errorfile [filename] \
Usage: python3 statusparser -f [List of URLs file] --noerrors

**StatusCode** \
Note: Only return certain status codes. \
Note: Errors will still print, unless suppressed with --noerrors
Usage: python3 statusparser -f [List of URLs file] -s 200 404 403 (..etc, NO commas)


# Common Status Codes You May Come Across:
| Status Code | Description |
| --- | --- |
| 200 | OK |
| 301 | Moved |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 410 | Gone |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

# Version
[![VersionNumber](https://img.shields.io/badge/Version-2.2.1-dark_green.svg)](https://shields.io/)

# License
[![LicenseNumber](https://img.shields.io/badge/License-MIT-dark_green.svg)](https://shields.io/)

# Author:
Matthew Greer

<a href="https://www.buymeacoffee.com/dfc302" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
