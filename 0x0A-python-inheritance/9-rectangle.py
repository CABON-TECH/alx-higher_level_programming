#!/usr/bin/python3
'''
Module contains Rectangle Class
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    A rectangle class
    '''
    def __init__(self, width, height):
        '''
        args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''
        Returns area of the Rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Returns string representation of the Rectangle
        '''
        return "[{}] {}/{}".format(type(self).__name__, self.__width,
                                   self.__height)
