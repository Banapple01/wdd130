"""
File: week3.py
Author: Jonathan Wright

Purpose: checking and changing data types.
"""

age = int(input("How old are you? ")) + 1
print(f'On your next birthday, you will be {age}')

eggs = int(input("\nHow many egg cartons do you have? ")) * 12
print(f'You have {eggs} eggs')

cookies = float(input("\nHow many cookies do you have? "))
people = float(input("how many people are there? "))
share = "%.2f" % (cookies/people)
print(f'Each person may have {share} cookies')