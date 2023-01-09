#!/usr/bin/python3
'''
Module contains lookup function
'''


def lookup(obj):
    '''Lists all attributes and methods of an object
    args:
        obj (object): The object whose attributes and methods are to be listed
    Returns:
        list: A list of all the attributes and methods
    '''
    return dir(obj)
