#!/usr/bin/python3
"""
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.encode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
