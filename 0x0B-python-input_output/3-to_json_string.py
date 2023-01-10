#!/usr/bin/python3
'''
Module contains a function for serializing a python object
'''
import json


def to_json_string(my_obj):
    '''
    Serializes a python object
    Args:
        my_obj (object): The object to be serialized
    '''
    return json.dumps(my_obj)
