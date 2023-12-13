#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:07:25 2021

@author: Ayah League

Homework 1: Lab 1 (9/25)
"""
user_input = int(input())

if 11 <= user_input <= 100:
    while user_input % 11 != 0:
        user_input -= 1
        print(user_input)
else:
    print("Input must be 11-100")
        