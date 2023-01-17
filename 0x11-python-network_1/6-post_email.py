#!/usr/bin/python3

"""This is  a Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""



import sys
import requests

if name == "main":
url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}

r = requests.post(url, data=data)
print(r.text)