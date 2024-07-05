#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""

import sys

from urllib import request, parse


if __name__ == '__main__':
    url, email = sys.argv[1:]

    email = parse.urlencode({'email': email}).encode('UTF-8')
    req = request.Request(url, data=email, method='POST')
    with request.urlopen(req) as res:
        body = res.read()
    print(body.decode())
