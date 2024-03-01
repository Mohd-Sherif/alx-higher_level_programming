#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys

import requests


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username, password = sys.argv[1:]

    response = requests.get(url, auth=(username, password))

    print(response.json()['id'])
