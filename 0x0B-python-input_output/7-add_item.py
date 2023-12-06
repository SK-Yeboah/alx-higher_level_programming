#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os  # Import the os module to check file existence

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    # Check if the file exists
    if os.path.exists(filename):
        try:
            items = load_from_json_file(filename)
        except ValueError:
            # Handle the case where the file contains invalid JSON
            print(f"Error: {filename} contains invalid JSON.")
            sys.exit(1)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
