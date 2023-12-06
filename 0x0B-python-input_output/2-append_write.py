#!/usr/bin/python3
"""Defines file-appending function"""
def append_write(filename="", text=""):
      """
    Appends the given text to the end of a text file (UTF-8) and returns the number of characters added.

    Parameters:
    - filename (str): The name of the file to which the text will be appended. If the file doesn't exist, it will be created.
    - text (str): The text to append to the file.

    Returns:
    - int: The number of characters added to the file.

    """
      with open(filename, 'a', encoding='utf-8') as file:
          return file.write(text)
              

