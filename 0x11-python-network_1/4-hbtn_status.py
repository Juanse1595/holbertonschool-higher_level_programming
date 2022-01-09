#!/usr/bin/python3
"""4-hbtn_status module"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    outp_str = r.content.decode('utf-8')
    print("Body response:\n\
          \t- type: {}\n\
          \t- content: {}".format(type(outp_str), outp_str))
