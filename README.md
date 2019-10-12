[![Follow on Twitter](https://img.shields.io/twitter/follow/Vail__.svg?logo=twitter)](https://twitter.com/Vail__)

# StatusParser
Retrive the status codes from a list of URLs

# Installation:
git clone https://github.com/DFC302/statusparser.git

cd statusparser/ \
sudo chmod 755 statusparser.py

# Requirements
Python3

**Modules**\
requests \
argparse \
sys \
concurrent.futures \
socket \
colorama

# Usage:
```
usage: urlparser.py [-h] [-f FILE] [-o OUT] [-t THREADS] [-d]
                    [--timeout TIMEOUT]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Specify input file containing list of URLs
  -o OUT, --out OUT     Specify output file.
  -t THREADS, --threads THREADS
                        Specify number of threads.
  --timeout TIMEOUT     Specify number in seconds for URL timeout.
```

# Example Usage:
python3 statusparser.py -h **Display help menu** \
python3 statusparser.py -f [**file containing URLS**] -t [**OPTIONAL: Number of threads #Default is 10**] -o [**write to file**] --timeout [**Specify request timeout**]

# Status Codes:
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

# Author:
Matthew Greer
