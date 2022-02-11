"""
File: positive.py
Author: Jonathan Wright

Purpose: be positive.
"""

number = -1
while number <0:
    number = int(input("Please type a positive number: "))
    if(number <0):
        print("Sorry, that is a negative number. Please try again.")
    else:
        print(f'The number is: {number}\n')