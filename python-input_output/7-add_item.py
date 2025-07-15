#!/usr/bin/python3
"""A script using Functions to add imported arguments to a list"""

import sys
import json
dumps_in_5 = __import__('5-save_to_json_file').save_to_json_file
loads_in_6 = __import__('6-load_from_json_file').load_from_json_file
""""""
try:
    json_list = loads_in_6("add_item.json")
except FileNotFoundError:
    json_list = []
json_list = json_list + sys.argv[1:]
dumps_in_5(json_list, "add_item.json")
