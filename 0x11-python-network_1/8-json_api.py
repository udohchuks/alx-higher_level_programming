#!/usr/bin/python3
"""cript that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user"""

import requests
import sys

letter = sys.argv[1] if len(sys.argv) > 1 else ""

data = {
    "q": letter
}

response = requests.post("http://0.0.0.0:5000/search_user", data=data)
try:
    json_response = response.json()
    if json_response:
        print(f"[{json_response.get('id')}] {json_response.get('name')}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
