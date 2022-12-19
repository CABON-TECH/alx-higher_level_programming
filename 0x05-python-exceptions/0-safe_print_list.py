#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    '''
    Prints X elements of a list
    '''
    count = 0
    try:
        for i in my_list[:x]:
            print("{}".format(i), end='')
            count += 1
    except IndexError:
        print('Oops')
    print()

    return count
