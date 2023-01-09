#!/usr/bin/python3
'''
Module contains empty class
'''


class BaseGeometry:
    '''
    An empty class BaseGeometry
    '''

    def area(self):
        '''
        Empty area method
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Validates integers
        Args:
            name (str): The name
            value (int): An integer value
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
