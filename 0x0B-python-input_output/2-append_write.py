#!/usr/bin/python3
'''
Module contains a function for appending to a text file
'''


def append_write(filename="", text=""):
    '''
    Appends some text to a file
    Args:
        filename (string): The name of the file to write to
        text (string): The text to add to the file
    '''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
