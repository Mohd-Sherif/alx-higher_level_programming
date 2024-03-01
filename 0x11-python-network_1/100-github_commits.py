#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge.
    - The first argument will be the repository name
    - The second argument will be the owner name
"""

import sys

import requests


if __name__ == '__main__':
    repo, owner = sys.argv[1:]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    commits = requests.get(url, params={'per_page': 10}).json()
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f'{sha}: {author}')
