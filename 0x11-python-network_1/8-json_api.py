#!/usr/bin/python3
"""8-json_api module"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        value = sys.argv[1]
    else:
        value = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': value})
    try:
        msg = r.json()
        if msg == {} or msg is None:
            print("No result")
        else:
            print("[{}] {}".format(msg['id'], msg['name']))
    except ValueError:
        print("Not a valid JSON")
