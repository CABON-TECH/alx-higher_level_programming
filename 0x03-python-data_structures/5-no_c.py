#!/usr/bin/python3
def no_c(my_string):
    return(my_string.translate({ord('C'): None, ord('c'): None}))
