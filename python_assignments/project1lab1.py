#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:39:08 2021

Project 1 Lab 1

Ayah League
"""

def print_menu():
    print("\nMENU \nc - Number of non-whitespace characters \nw - Number of words \nf - Fix capitalization \nr - Replace punctuation \ns - Shorten spaces \nq - Quit")
    
def execute_menu(user_choice, text):
    if user_choice == 'c':
        count = get_num_of_non_WS_characters(text)
        print("Number of non-whitespace characters:",count)
        return 0
    elif user_choice == 'w':
        count = get_num_of_words(text)
        print("Number of words:",count)
        return 0
    elif user_choice == 'f':
        count,newstr = fix_capitalization(text)
        print("Number of letters capitalized:",count)
        print("Edited text:",newstr)
        return 0
    elif user_choice == 'r':
        count1,count2,newstr = replace_punctuation(text,exclamation_count=0,semicolon_count=0)
        print("Punctuation replaced")
        print("exclamation_count:",count1)
        print("semicolon_count:",count2)
        print("Edited text:",newstr)
        return 0
    elif user_choice == 's':
        newstr = shorten_space(text)
        print("Edited text:",newstr)
        return 0
    elif user_choice == 'q':
        return 1 
    else:
        return 2
        

def get_num_of_non_WS_characters(string):
    count = 0
    for characters in string:
        if characters != ' ':
            count += 1
    return count
        
def get_num_of_words(string):
    count = 0
    for characters in string:
        if characters == ' ':
            count += 1
    return count

def fix_capitalization(string):
    new_string =''
    if string[0].islower():
        new_string += string[0].upper()
    n = len(string)
    i=1
    while(i<n):
        count=0
        if string[i] == '.' and i+1<n and string[i+1] == ' ' and i+2<n:
            new_string += string[i:i+2]
            if string[i+2].islower():
                new_string += string[i+2].upper()
                count+=1
            else:
                new_string += string[i+2]
            i+=3
        else:
            new_string += string[i]
            i+=1
    return count,new_string

def replace_punctuation(string, **kwargs):
    new_string=''
    exclamation_count = 0
    semicolon_count = 0
    for character in string:
        if character == '!':
            new_string += '.'
            exclamation_count += 1
        elif character == ';':
            new_string += ','
            semicolon_count += 1
        else:
            new_string += character
    return exclamation_count,semicolon_count,new_string
            
def shorten_space(string):
    new_string=''
    space = False
    n=len(string)
    for i in range(n):
        if string[i]!=' ':
            if space == True:
                if string[i]=='.' or string[i]=='?' or string[i]==',':
                    pass 
                else:
                    new_string += ' '
                space = False
            new_string += string[i]
        elif string[i-1] != ' ':
            space = True
    return new_string

def main():
    print("Enter the string : ")
    s=input()
    print("\nYou entered: ", s)
    print_menu()
    choice = input("Please select your choice: ")
    val = execute_menu(choice,s)
    while(val!=1):
        print_menu()
        choice = input("Please select your choice: ")
        val = execute_menu(choice,s)
        while(val==2):
            print("Invalid choice!")
            choice = input("Please select your choice: ")
            val = execute_menu(choice,s)
main()