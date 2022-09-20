#!/usr/bin/python3
"""Module 7-add_item
Will add all arguments to the Python list, then save them in the file
"""


import json
import sys
import os.path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


my_file = "add_item.json"
my_list = []


if os.path.exists(my_file):
    my_list = load_from_json_file(my_file)

for elem in range(1, len(sys.argv)):
    my_list.append(sys.argv[elem])

save_to_json_file(my_list, my_file)
