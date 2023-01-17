#!/user/bin/python3

import urllib.request

if name == "main":
req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as resp:
body = resp.read()
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
