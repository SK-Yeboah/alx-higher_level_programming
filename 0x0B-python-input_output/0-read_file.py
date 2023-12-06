#!/usr/bin/python3
"""Definning the text reading-file function"""

def read_file(filename=""):
    """Openning and reading contents of UTF8 text file to stdout"""
    with open(filename, 'r', encoding = "utf-8") as file:
        print(file.read(), end="")
