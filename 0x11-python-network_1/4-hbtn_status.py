#!/usr/bin/python3
"""4-hbtn_status module"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    outp_str = r.content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(outp_str)))
    print("\t- content: {}".format(outp_str))
