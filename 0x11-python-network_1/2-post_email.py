#!/usr/bin/python3

"""
 sends a POST request to the passed URL with the email as a parameter,
 and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        'email': email
        }
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    with urllib.request.urlopen(url, data=encoded_data) as response:
        body = response.read()
        print(body.decode('utf-8'))
