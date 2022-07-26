#!/usr/bin/python3

str = input("Enter a string: ")
str = str.lower()
for i in str:
    i = ord(i) - 32
    print('{}'.format(chr(i)), end='')
