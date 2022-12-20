#!/usr/bin/python3
'''
Module of a Square class
'''


class Square:
    '''A simple class that defines a square
    Attributes:
        size: The size of the square
    '''

    def __init__(self, size=0):
        '''Initialization method for the Square class
        Args:
            size(int): The size of the square
        '''
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
