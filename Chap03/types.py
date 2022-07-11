#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = (1, 'two', 3.0, [4, 'four'], 5) #defining a tuple called x
y = (1, 'two', 3.0, [4, 'four'], 5) #defining a identical value tuple called y

print('X i s {}'.format(x))#prints the values of x
print('Type of x is {}'.format(type(x)))#prints the type of x
print('X i s {}'.format(y))#prints the values of y
print('Type of x is {}'.format(type(y)))#prints the values of y
print(f'Id of x is {id(x)}')#prints the ID of x
print(f'Id of y is {id(y)}')#prints the ID of y


for i in range(len(x)): #prints the individual elements on the x and y tuple
    print(id(x[i]))
    print(id(y[i]))

#ID function returns a unique identifier for each OBJECT
print(f'Id of x is {id(x)}')#prints the ID of x
print(f'Id of y is {id(y)}')#prints the ID of y

if isinstance(x, tuple):#The correct way to identify if an object is a type of a class
    print("X is a tuple")
elif isinstance(x,list):
    print("X is a list")