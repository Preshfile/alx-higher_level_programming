#!/usr/bin/python3

"""This is a script displays the value of the X-Request-Id variable 
found in the header of the response."""

import sys
from urllib.request import Request, urlopen

url = sys.argv[1]

request = Request(url)
with urlopen(request) as response:
    headers = dict(response.getheaders())
    x_request_id = headers.get("X-Request-Id")
    print(x_request_id)
