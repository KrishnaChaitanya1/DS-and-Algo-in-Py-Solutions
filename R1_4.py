# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:11:50 2018

@author: Krishna
"""
def sumofsquares(n):
    sumsqr=0
    for square in range(1, n):
        sumsqr += square*square
    return sumsqr

a = input("Enter the limit for sum of squares: ")
print("The Sum of squares: ", sumofsquares(int(a)))