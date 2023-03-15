#!/usr/bin/python3
"""Sends post request/email to url and displays"""
import sysimport urllib.request
if _name_ == "_main_":    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:        headers = response.info()        x_request_id = headers['X-Request-Id']
    print(x_request_id)
