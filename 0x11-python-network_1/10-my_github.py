#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user', auth=(username, password))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)

