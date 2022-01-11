"""
File: week1.py
Author: Jonathan Wright

Purpose: input output.
"""
first = input("What is your first name?: ")
last = input("What is your last name?: ")
if first == "James" and last == "Bond":
    print("It's an honor to meet you 007.")
else:
    print("Your name is", last + ",", first, last + ".")
# print(f"Your name is {last}, {first} {last}.")