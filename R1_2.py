# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:03:31 2018

@author: Krishna
"""

def is_even(k):
    if k % 2 == 0:
        return True
    return False

a = input("Enter a number: ")
print("Is Even? : ", is_even(int(a)))