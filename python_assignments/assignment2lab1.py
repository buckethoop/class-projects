#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 2 Lab 2

Ayah League (09/13/21)

"""

print ("Enter three values: ")

red = int(input())
green = int(input())
blue = int(input())

minimum = min(red,green,blue)

new_red = red - minimum
new_green = green - minimum
new_blue = blue - minimum

if new_red < 0:
    new_red = 0
if new_green < 0:
    new_green = 0
if new_blue < 0:
    new_blue = 0
    
print(new_red, new_green, new_blue)