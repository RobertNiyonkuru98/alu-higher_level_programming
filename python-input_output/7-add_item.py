#!/usr/bin/python3
'''script that adds all args to a python list and saves them to a file'''

import sys
save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
load_from_json_file = _import_('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

json_list.extend(sys.argv[1:])

save_to_json_file(json_list, filename)
