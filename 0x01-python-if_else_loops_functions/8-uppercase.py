#!/usr/bin/python3
def uppercase(str):
    for n in str:
        n = ord(n)
        if n >= 97 and n <= 122:
            n -= 32
        n = chr(n)
        print("{}".format(n), end='')
    print("")
