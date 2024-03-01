#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as req


if __name__ == '__main__':
    with req.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
    print('Body response:')
    print('    - type: {}'.format(type(body)))
    print('    - content: {}'.format(body))
    print('    - utf8 content: {}'.format(body.decode()))
