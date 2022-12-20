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

    @property
    def size(self):
        '''The getter function for the size attribute
        Returns:
            size
        '''
        return self.__size

    @size.setter
    def size(self, val):
        '''The setter function for the size attribute
        Args:
            value: The value to be set as the size
        '''
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        '''Finds the area of the Square
        Returns:
            The area of the square
        '''
        return self.__size ** 2
