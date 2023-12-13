#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:54:21 2021

@author: buckethoop
"""

user_int1 = int(input("Enter Integer: "))
result0 = "You entered: {}"
print(result0.format(user_int1))

int1_squared = user_int1 * user_int1
int1_cubed = user_int1 * user_int1 * user_int1
result1 = "{0} squared is {1} And {0} cubed is {2} !!"
print(result1.format(user_int1,int1_squared,int1_cubed))

user_int2 = int(input("Enter another integer: "))
sum_of_ints = user_int1 + user_int2
product_of_ints = user_int1 * user_int2 
result2 = "{0} + {1} is {2}"
result3 = "{0} * {1} is {2}"
print(result2.format(user_int1, user_int2, sum_of_ints))
print(result3.format(user_int1, user_int2, product_of_ints))

