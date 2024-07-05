#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys

import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = "" if len(sys.argv) <= 1 else sys.argv[1]

    response = requests.post(url, data={'q': q})

    if response.headers['content-type'] == 'application/json':
        res_json = response.json()
        if res_json:
            print('[{}] {}'.format(res_json['id'], res_json['name']))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
