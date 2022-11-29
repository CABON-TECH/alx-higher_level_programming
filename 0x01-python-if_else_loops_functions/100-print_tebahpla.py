#!/usr/bin/python3

for i in range(122, 96, -1):
    x = 32
    if i % 2 == 0:
        x = 0
    print("{}".format(chr(i - x)), end="")
