#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("Value is {}".format(int(value)));
        return True
    except Exception as e:
        print("Exception: {}".format(e), file =sys.stderr)
        return False

