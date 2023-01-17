#!/usr/bin/python3


"""This is a Python script that takes in a letter 
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests
if name == "main":
url = sys.argv[1]
response = requests.get(url)
if response.status_code >= 400:
print("Error code: {}".format(response.status_code))
else:
print(response.text)
