#!/usr/bin/python3
"""Sends a POST request to a specified URL with a given letter as a parameter.
Usage: ./8-json_api.py <url> <letter>

The letter is sent as the value of the variable q.
If no letter is provided, sends q="".
"""

#!/usr/bin/python3
"""Sends a POST request to a specified URL with a given letter as a parameter.
Usage: ./8-json_api.py <url> <letter>

The letter is sent as the value of the variable q.
If no letter is provided, sends q="".
"""
import sys
import requests
if name == "main":
url = sys.argv[1]
letter = "" if len(sys.argv) == 2 else sys.argv[2]
payload = {"q": letter}

r = requests.post(url, data=payload)
try:
    response = r.json()
    if response == {}:
        print("No result")
    else:
        print("[{}] {}".format(response.get("id"), response.get("name")))
except ValueError:
    print("Not a valid JSON")
