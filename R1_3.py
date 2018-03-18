# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:05:02 2018

@author: Krishna
"""

def minmax(data):
    dmin = dmax = data[0]
    for val in data[1:]:
        if val < dmin:
            dmin = val
        if val > dmax:
            dmax = val
    return dmin, dmax

inputs = input("Enter the numbers: ")
data = [int(d) for d in inputs.split()]
min_max = minmax(data)
print(" Minimum: {}, Maximum: {}".format(min_max[0], min_max[1]))