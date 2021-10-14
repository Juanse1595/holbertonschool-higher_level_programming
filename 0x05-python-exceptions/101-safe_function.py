#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, TypeError, ValueError, IndexError) as err0r:
        print("Exception: {}".format(err0r), file=sys.stderr)
        return None
