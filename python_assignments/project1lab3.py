#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:39:05 2021

Project 1 Lab 3

Ayah League
"""

import random

def main():
    print("This is a number guessing game.")
    print("Guess what number we thought of between 1 and 100")
    guessing_game()
    
def guessing_game():
    answer = random.randint(1, 101)
    tries = 0 
    end = "You guessed {} times".format(tries)
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < answer:
            print("Too low, try again")
            tries += 1
        
            
        elif guess > answer:
            print("Too high, try again")
            tries += 1
        
        
        else:
            tries += 1
            break
    
    end = "You guessed {} times".format(tries)
    print("Congrats")
    print (end)
main()