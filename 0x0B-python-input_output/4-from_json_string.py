#!/usr/bin/python3
'''
Module contains a function for deserializing JSON
'''
import json


def from_json_string(my_str):
    '''
    Serializes a python object
    Args:
        my_str : The JSON to be deserialized
    '''
    return json.loads(my_str)
