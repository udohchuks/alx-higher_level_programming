#!/usr/bin/python3
"""json

load to file
"""
import json


def load_from_json_file(filename):
    """
    load json file to file
    """
    with open(filename, "r") as f:
        return json.load(f)
