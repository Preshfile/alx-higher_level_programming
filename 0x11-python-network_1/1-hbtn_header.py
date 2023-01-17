#!/usr/bin/python3

"""This is a script displays the value of the X-Request-Id variable 
found in the header of the response."""

import sys
import urllib.request

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    print(dict(res.headers).get("X-Request-Id"))
