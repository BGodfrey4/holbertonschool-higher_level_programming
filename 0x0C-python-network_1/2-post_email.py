#!/usr/bin/python3
"""
script will send a post request to give url and email & show decoded
body of the response
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    givenurl = argv[1]
    email = argv[2]
    datadict = {'email': email}
    encodeddata = urlencode(datadict)
    utf8data = encodeddata.encode("utf-8")

    with urlopen(givenurl, data=utf8data) as response:
        body = response.read()
        print(body.decode("utf-8"))
