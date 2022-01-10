#!/usr/bin/python3
"""10-my_github module"""
import sys
import requests


if __name__ == '__main__':
    owner = sys.argv[1]
    url = "https://api.github.com/users/{}".format(owner)
    r = requests.get(url)
    print(r.json()['id'])
