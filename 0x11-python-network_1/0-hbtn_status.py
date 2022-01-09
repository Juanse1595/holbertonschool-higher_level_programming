#!/usr/bin/python3
"""0-hbtn_status module"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        outp = response.read()
        print("Body response:\n\
                - type: {}\n\
                - content: {}\n\
                - utf8 content: {}".format(type(outp), outp,
                                           outp.decode('utf-8')))
