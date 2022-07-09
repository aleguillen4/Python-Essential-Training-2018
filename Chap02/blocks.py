#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from random import randint as ri #importing the only function the programm will use

x = ri(0,100)#declaring a new random variable between 0 and 100
y = ri(0,50)#declaring a new random variable between 0 and 50
print(f"X is: {x} and Y is: {y} ")

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))#one way to use format
elif x > y:
    print(f"x > y: x = {x} , y = {y}")#other way to use formated strings, I like this one better
