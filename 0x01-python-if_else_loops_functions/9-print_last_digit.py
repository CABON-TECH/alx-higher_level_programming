#!/usr/bin/python3
def print_last_digit(number):
    '''
    Prints the last digit of a number.
    '''
    n = abs(number) % 10
    print(n, end="")
    return n
