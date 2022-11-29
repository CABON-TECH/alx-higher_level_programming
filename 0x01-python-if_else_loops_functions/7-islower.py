#!/usr/bin/python3
def islower(c):
    '''
    CHecks whether charcater passed to it is lowercase or uppercaase
    '''
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
