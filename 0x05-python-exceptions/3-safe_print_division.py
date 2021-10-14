#!/usr/bin/python3
def safe_print_division(a, b):
    divi_result = 0
    try:
        divi_result = a / b
    except ZeroDivisionError:
        divi_result = None
    finally:
        print("Inside result: {}".format(divi_result))
    return divi_result
