#!/usr/bin/python3
if __name__ == "__main__":
    """Print the additions of all args"""

    import sys

    arg_num = len(sys.argv) - 1
    total = 0
    for i in range(arg_num):
        total += int(sys.argv[i+1])
    print("{}".format(total))
