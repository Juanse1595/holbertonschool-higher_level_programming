#!/usr/bin/python3
"""0-hbtn_status module"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        outp = response.read()
        print("Body response:")
        print("- type: {}".format(type(outp)))
        print("- content: {}".format(outp))
        print("- utf8 content: {}".format(outp.decode('utf-8')))
