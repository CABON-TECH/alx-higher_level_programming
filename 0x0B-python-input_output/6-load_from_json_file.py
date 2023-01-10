#!/usr/bin/python3
'''
Module contains function for creating python object from json file
'''
import json


def load_from_json_file(filename):
    '''
    Creates a Python object from a json file
    Args:
        filename (string): The name of the json file to be read
    '''
    with open(filename, encoding='utf-8') as f:
        json_string = f.read()
        return json.loads(json_string)
