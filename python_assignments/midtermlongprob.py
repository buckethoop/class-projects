#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:09:32 2021

Midterm Long Programming Question
"""
import random
import math

def getChoice(x,y,z):
    choices = [x, y, z]
    print(random.sample(choices,1))

def myMath(a=1,b=4,c=0):
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print( x1, x2 )
    
    
    
def get_acronym(x,y,z):
    acronym = ''
    words = [x,y,z]
   
    for item in words:
        if len(item) > 0:
            acronym += item[0]         
            
    print(acronym.upper())


def main():
    getChoice("hi", "bye", "why")
    getChoice("", "random", "null")
    getChoice(1,3,"hoho")
    myMath(1,4,4)
    myMath(4,1)
    myMath()
    get_acronym("random","access", "memory")
    get_acronym("central","processing", "unit")
    get_acronym("","haha", "bye")
    
if __name__ == '__main__':
    main()