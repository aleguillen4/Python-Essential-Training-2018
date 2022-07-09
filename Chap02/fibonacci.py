#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1# positional assignation
""" Equivalent way
a = 0
b = 1
"""
while b < 1000:
    print(b, end = ' ', flush = True) #formating so it prints a single line
    a, b = b, a + b

print() # line ending
