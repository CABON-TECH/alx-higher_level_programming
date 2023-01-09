#!/usr/bin/python3
'''
Module contains My_list class
'''


class MyList(list):
    '''
    List object
    Methods:
        print_sorted: Prints a sorted list
    '''

    def print_sorted(self):
        '''
        Prints a sorted list
        '''
        print(sorted(self))
