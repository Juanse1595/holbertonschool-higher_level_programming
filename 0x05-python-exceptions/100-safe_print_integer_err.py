#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err0r:
        print("Exception: {}".format(err0r), file=sys.stderr)
        return False
    return True
