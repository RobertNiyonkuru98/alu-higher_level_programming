#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        return raise_exception_msg()
    except NameError:
        print("Error Message")
