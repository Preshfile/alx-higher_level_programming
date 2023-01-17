#!/usr/bin/python3

"""This is a script displays the value of the X-Request-Id variable 
found in the header of the response."""

import sys
import urllib.request

if name == "main":
url = sys.argv[1]

request = urllib.request.urlopen(url)
headers = request.info()
print(headers.get("X-Request-Id"))
