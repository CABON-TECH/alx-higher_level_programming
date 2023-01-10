#!/usr/bin/python3
'''
Module contains a function for writing serialized data to a text file
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Writes serialized data to a text file
    Args:
        my_obj :The python object to serialize
        filename: The name of the file to write to
    '''
    with open(filename, mode='w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
