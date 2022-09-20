#!/usr/bin/python3
"""
    will add all arguments to the Python list,
    then save them to the file in JSON format
"""
import sys
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

FILE = "add_item.json"

try:
    my_list = load_json(FILE)
except (FileNotFoundError, TypeError):
    my_list = []

for i in sys.argv[1:]:
    my_list.append(i)

save_json(my_list, FILE)
