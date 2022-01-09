#!/usr/bin/python3
"""3-error_code module"""
import urllib.request
import urllib.error
import sys


req = urllib.request.Request(sys.argv[1])
try:
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print('Error code: {}'.format(e.code))
