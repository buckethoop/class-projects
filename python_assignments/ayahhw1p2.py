#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:59:09 2021

@author: buckethoop
"""
radius = float(input("Enter a radius: "))
rad_cubed = radius * radius * radius
sphere_volume = (4.0/3.0) * 3.14 * rad_cubed
print("Sphere Volume: %f" %(sphere_volume))