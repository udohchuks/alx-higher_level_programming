#!/usr/bin/python3
""" sends a request to the URL and displays the value of the X-Request-Id"""

import urllib.request
import sys
url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_requested_id = response.headers.get('X-Request-Id')
print(x_requested_id)
