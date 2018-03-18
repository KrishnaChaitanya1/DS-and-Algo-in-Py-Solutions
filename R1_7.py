# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:23:53 2018

@author: Krishna
"""

def sumofoddsquare(n):
    return sum(val ** 2 for val in range(1, n, 2))

a = input("Enter the Limit: ")
print("The Sum of Square of Odd: ", sumofoddsquare(int(a)))