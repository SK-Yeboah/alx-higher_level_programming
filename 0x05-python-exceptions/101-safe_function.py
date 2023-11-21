#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except ZeroDivisionError:
        print("Exception: Division by zero", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
