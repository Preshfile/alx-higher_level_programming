#!/usr/bin/python3

"""This is a Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

auth = requests.auth.HTTPBasicAuth(username, token)

response = requests.get("https://api.github.com/user", auth=auth)

if response.status_code == 200:
    
    user_id = response.json().get("id")
    print(user_id)
else:
    print(None)

