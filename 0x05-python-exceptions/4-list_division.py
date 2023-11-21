# !/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(0, list_length):
        try:
            division_result = float(my_list_1[i]) / float(my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except (TypeError, ValueError):
            print("invalid input type or value")
            result_list.append(0)
        except IndexError as e:
            print("index out of range", str(e))
            result_list.append(0)
        else:
            result_list.append(division_result)
        finally:
            pass
    return result_list
