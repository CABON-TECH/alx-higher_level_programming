#!/usr/bin/python3
s = 0
for i in range(10):
    for n in range(s, 10):
        if i == n:
            continue
        if i == 8 and n == 9:
            print("{:d}{:d}".format(i, n))
        else:
            print("{:d}{:d}".format(i, n), end=", ")
    s = s + 1
