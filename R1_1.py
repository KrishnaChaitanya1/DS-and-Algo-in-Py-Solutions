# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 21:59:53 2018

@author: Krishna
"""

def is_multiple(n, m):
    if n % m ==0:
        return True
    return False

a, b = input("Enter two numbers: ").split()
print("Is multiple?: ", is_multiple(int(a), int(b)))