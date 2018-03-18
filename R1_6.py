# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:20:48 2018

@author: Krishna
"""

def sumofsquareodd(n):
    sumsqr = 0
    for val in range(1, n, 2):
        sumsqr += val ** 2
    return sumsqr

a = input("Enter the Limit: ")
print("The Sum of Squares of Odd: ", sumofsquareodd(int(a)))