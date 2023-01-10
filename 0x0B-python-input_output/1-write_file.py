#!/usr/bin/python3
'''
Module contains a function for writing to a text file
'''


def write_file(filename="", text=""):
    '''
    Writes some text to a file
    Args:
        filename (string): The name of the file to write to
        text (string): The text to add to the file
    '''
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
