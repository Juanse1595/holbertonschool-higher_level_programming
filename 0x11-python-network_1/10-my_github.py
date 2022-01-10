#!/usr/bin/python3
"""10-my_github module"""
import sys
import requests


if __name__ == '__main__':
    owner = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/users/{}".format(owner)
    headers = {'Authorization': 'token {}'.format(passwd)}
    r = requests.get(url, headers=headers)
    if r:
        print(r.json()['id'])
    else:
        print('None')
