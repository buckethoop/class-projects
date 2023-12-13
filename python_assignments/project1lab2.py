#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:11:46 2021

Project 1 Lab 2

Ayah League
"""

import math 

tries = 0

while(tries<3):
    x0, y0 = list(map(int,input("Enter x and y coordinates of 1st circle:").split()))
    r0 = int(input("Enter radius of 1st circle: "))
    x1, y1 = list(map(int,input("Enter x and y coordinates of 2nd circle:").split()))
    r1 = int(input("Enter radius of 2nd circle: "))
    
    if x0 >= 0 and y0 >= 0 and x1 >= 0 and y1 >=0:
        d = math.sqrt((x1-x0)**2 + (y1-y0)**2)
        
        if d > r0+r1:
            print("Two circles don't intersect and are entirely serperate.")
        elif d < abs(r0-r1) :
            print("Two circles do not intersect and one is contained within other")
        elif d == r0+r1 :
            print("Two cicles intersect a single point")
        elif d == 0 and r0 == r1 :
            print("Two circles are coincident")
        else :
            print("Two circles intersect at two point")
        break
    
    else:
        print("Invalid coordinates enter again.")
        tries += 1
print("Bye.")