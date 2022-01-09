#!/usr/bin/python3
"""3-error_code module"""
from urllib import request, error
import sys


if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
