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

    def to_json(self):
        return self.__dict__
