#!/usr/bin/python3
"""1-hbtn_header module"""
import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.headers.get('X-Request-Id'))
