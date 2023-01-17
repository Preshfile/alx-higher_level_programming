#!/usr/bin/python3

"""This is a Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

# Use Basic Authentication with the personal access token
response = requests.get('https://api.github.com/user', auth=(username, token))

if response.status_code == 200:
    # Get the id from the response JSON
    user_id = response.json().get('id')
    print(user_id)
else:
    print(None)

