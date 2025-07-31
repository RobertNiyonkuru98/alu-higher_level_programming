#!/usr/bin/python3
"""
This module fetches the status from a given URL using urllib.

It sends a GET request to 'https://intranet.hbtn.io/status' with custom headers,
reads the response, and prints information about the response body:
    - the type of the response content
    - the raw content
    - the decoded content in UTF-8

Example output:
    Body response:
        - type: <class 'bytes'>
        - content: b'...'
        - utf8 content: ...
"""

import urllib.request

url = "https://intranet.hbtn.io/status"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    '\n ApplewebKit/537.36 (KHTML, like Gecko) '
    '\n Chrome/99.0.4844.84 Safari/537.36',
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
