"""
File: candy.py
Author: Jonathan Wright

Purpose: Ask nicely.
"""

candy = "no"
while candy != "yes":
    candy = input("May I have a piece of candy? ").lower()
    if(candy == "yes"):
        print("Thank you.")
    else:
        candy = "no"