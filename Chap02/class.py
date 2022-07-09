#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck: #New class created
    def quack(self):#describing a method
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')#describing a method
def main():
    donald = Duck()#creating a new object
    donald.quack()#calling a method
    donald.walk()#calling a method

if __name__ == '__main__': main()
