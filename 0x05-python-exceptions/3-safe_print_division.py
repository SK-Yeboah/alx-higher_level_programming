#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division is not allowed")
        return None
    except Exception as e:
        print(f"Am error occured at: {e}")
        return None
    else:
        print("Inside result: {:d}".format(result))
        return result
    finally:
        print("Finally: Division operation has completed")
