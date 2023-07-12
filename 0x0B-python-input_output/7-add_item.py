#!/usr/bin/python3
"""load and sav"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_list = []

argc = len(sys.argc)

if argc > 1:
    for i in range(1, argc):
        existing_list.append(sys.argv[i])

save_to_json_file(existing_list, "add_item.json")
