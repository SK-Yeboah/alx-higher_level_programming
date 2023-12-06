#!/usr/bin/python3

"""Definning the function to write a file"""

def write_file(filename = "", text = " "):
    """This is a function that writes a file with given filename and content."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
