#!/usr/bin/python3
"""Definning function to load from json file"""
import json


def load_from_json_file(filename):
    """Creates an object from the JSON representation stored in a file."""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
