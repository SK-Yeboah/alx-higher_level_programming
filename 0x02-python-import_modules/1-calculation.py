#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, dif , mul and quot of 10 and 5"""
    from  calculator_1 import add , subtract , multiply , divide

    a = 10
    b = 5

    sum_result = add(a, b)
    subtract_result = sub(a,b)
    mul_result = mul(a,b)
    div_result = div(a, b)

    print(f"{a} + {b} = {sum_result}")
    print(f"{a} - {b} = {subtract_result}")
    print(f"{a} * {b} = {mul_result}")
    print(f"{a} / {b} = {div_result}")
