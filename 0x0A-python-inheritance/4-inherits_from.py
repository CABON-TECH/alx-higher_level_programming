#!/usr/bin/python3
'''
Module contains for checking the instance of an object
'''


def inherits_from(obj, a_class):
    '''
    Returns True if the object is exactly an instance of the specified class
    args:
        obj: The object to check the instance for
        a_class: The class to compare the object with
    Returns:
        boolean: True if object is exactly an instance of the specified class
    '''
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
