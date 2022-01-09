#!/usr/bin/python3
"""7-error_code module"""
import sys
import requests


if __name__ == '__main__':
    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.content.decode('utf-8'))
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
