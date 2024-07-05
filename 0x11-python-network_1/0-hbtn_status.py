#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as req


if __name__ == '__main__':
    with req.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
    print('\t- utf8 content: {}'.format(body.decode()))
