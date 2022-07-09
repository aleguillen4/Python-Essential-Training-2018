#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n): #defines the isprime function which has n as an argument
    if n <= 1: #no natural prime is <1
        return False
    for x in range(2, n):#a for that iterates between 2 and n
        if n % x == 0: #x iterates and is used to check if the mod == 0 
            print(f"{n} is divisible by {x}") #prints which is the first number that n is divisible in
            return False
    else:
        return True

n = 351
if isprime(n):
    print(f'{n} is prime')#formated string
else:
    print(f'{n} not prime')