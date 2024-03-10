#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    response = requests.post(url, data=payload)
    print("Your email is:", response.text)

