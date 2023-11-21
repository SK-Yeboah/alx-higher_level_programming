#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Exception raised")
    except Exception as e:
        print(f"Caught an exceptin: {e}")
