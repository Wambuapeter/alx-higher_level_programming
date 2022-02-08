#!usr/bin/python3
'''reads a file'''


def read_file(filename=""):
    '''use with to automatically close'''
    with open(filename, encoding="utf-8") as myFile:
        read_data = myFile.read()
        print(read_data, end="")
