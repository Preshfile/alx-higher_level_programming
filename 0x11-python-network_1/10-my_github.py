#!/usr/bin/python3

"""This is a Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API to display your id
"""

#!/usr/bin/python3
import requests
import sys

# Get username and personal access token from command line arguments
username = sys.argv[1]
token = sys.argv[2]

# Set up basic authentication with the personal access token
auth = requests.auth.HTTPBasicAuth(username, token)

# Make a GET request to the GitHub API to retrieve the user's information
response = requests.get("https://api.github.com/user", auth=auth)

# Check if the request was successful
if response.status_code == 200:
    # Extract the user's id from the response
    user_id = response.json().get("id")
    print(user_id)
else:
    print(None)

