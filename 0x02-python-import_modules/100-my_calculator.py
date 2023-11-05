#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Define a dictionary with operators as keys and functions as values
    operands = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # Check if the provided operator is in the dictionary
    if operator not in operands:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    # Perform the calculation using the selected function from the dictionary
    result = operands[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))

