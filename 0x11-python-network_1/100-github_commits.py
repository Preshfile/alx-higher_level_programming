#!/usr/bin/python3

"""This is evaluates candidates applying for a back-end position
with multiple technical challenges, like this one:
    """

import requests
import sys

repo_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
response = requests.get(url)

commits = response.json()

for commit in commits[:10]:
    sha = commit["sha"]
    author = commit["commit"]["author"]["name"]
    print(f"{sha}: {author}")

