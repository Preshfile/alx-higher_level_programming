#!/usr/bin/python3

"""This is a Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""

import getpass
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = input("Enter your GitHub username: ")
    password = getpass.getpass(prompt="Enter your GitHub password: ")
    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
