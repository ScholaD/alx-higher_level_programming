#!/usr/bin/python3
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """  This function evaluates to True when the object is either an instance of the specified class or an instance of a class that inherits from the specified class; otherwise, it evaluates to False.  """
    return isinstance(obj, a_class)
