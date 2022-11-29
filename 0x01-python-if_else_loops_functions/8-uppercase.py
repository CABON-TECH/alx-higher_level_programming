#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    str2 = ''
    for character in str:
        character = ord(character)
        if character in range(97, 123):
            character -= 32
        str2 += chr(character)
    print("{:s}".format(str2))
