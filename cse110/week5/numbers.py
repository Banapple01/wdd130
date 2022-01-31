"""
File: numbers.py
Author: Jonathan Wright

Purpose: Gimme some numbers. And your favorite animal.
"""

number1 = int(input("What is the first number? "))
number2 = int(input("What is the second number? "))

g1 = False
equal = False
g2 = True

if(number1 == number2):
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")
elif(number1 > number2):
    print("The first number is greater")
    print("The numbers are not equal")
    print("The second number is not greater")
else:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")

ani = input("\nWhat's your favorite animal? ").lower()

if(ani == 'dog'):
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.\n")