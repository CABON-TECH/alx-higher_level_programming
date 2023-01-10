#!/usr/bin/python3
'''
Module contains a class Student
'''


class Student:
    '''
    Defines a Student
    Attributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Initializes the Student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Returns a dictionary representation of a Student instance
        Args:
            attrs (list): A list of required attributes
        '''
        new_dict = {}
        if attrs is not None:
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dict[k] = v
            return new_dict
        else:
            return self.__dict__
