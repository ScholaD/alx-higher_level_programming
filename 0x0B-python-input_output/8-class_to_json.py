#!/usr/bin/python3


def class_to_json(obj):
    """ function that returns the dictionary
    description
    """
    dics = {}
    if hasattr(obj, "__dict__"):
        dics = obj.__dict__.copy()
    return dics
