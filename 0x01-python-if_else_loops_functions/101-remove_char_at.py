#!/usr/bin/python3

def remove_char_at(str, n):
    s = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        s = s + str[i]
    return s
