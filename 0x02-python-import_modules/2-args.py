#!/usr/bin/python3
if __name__ == "__main__":
    """Print the list of Arguments """
    import sys

    arg_num = len(sys.argv)-1

    if arg_num == 0:
       print("0 argument.")
    elif arg_num  == 1:
       print(" 1 argument")
    
    for i in  range (arg_num):
        print("{}: {}".format(i+1, sys.argv[i+1]))
