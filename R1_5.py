# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:18:07 2018

@author: Krishna
"""

def sumofsquares(k):
        return sum(val ** 2 for val in range(1, k) if k > 0)

a = input("Enter the limit: ")
print("The Sum of squares: ", sumofsquares(int(a)))