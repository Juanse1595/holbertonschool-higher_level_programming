#!/usr/bin/python3
"""3-error_code module"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv


req = Request(argv[1])
try:
    response = urlopen(req)
    print(response.read().decode('utf-8'))
except HTTPError as e:
    print('Error code: {}'.format(e.code))
