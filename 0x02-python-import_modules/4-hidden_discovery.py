#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names of modules define in the hidden"""

    import hidden_4

    modules = dir(hidden_4)

    for names in modules:
        if names[:2] != "__":
            print(names)
