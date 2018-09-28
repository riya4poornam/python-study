#!/usr/bin/env python

def get_even():
    '''
    Function to print even numbers
    '''
    even = []
    for i in range(10):
        if i%2 == 0:
            even.append(i)
    return even

print get_even()
