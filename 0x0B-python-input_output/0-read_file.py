#!/usr/bin/python3
'''
Module contains a function for reading a text file
'''


def read_file(filename=""):
    '''
    Reads a file and prints the contents to stdout
    args:
        filename (string): The name of the file to be read
    '''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
