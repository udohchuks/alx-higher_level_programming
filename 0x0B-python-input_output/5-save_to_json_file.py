#!/usr/bin/python3
"""json

save json to file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to json file
    """
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
