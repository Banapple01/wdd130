"""
File: loan.py
Author: Jonathan Wright

Purpose: should you get a loan?
"""

how_large = int(input("How large is the loan? (1-10): "))
credit = int(input("How good is your credit history? (1-10): "))
income = int(input("How high is your income? (1-10): "))
down_pay = int(input("How large is your down payment? (1-10): "))

if how_large >= 5:
    if credit >= 7 and income >= 7:
        print("you get a loan!")
    elif credit >= 7 or income >= 7:
        if down_pay >= 5:
            print("You get a loan!")
        else:
            print("Sorry, your down payment isn't large enough.")
    else:
        print("Sorry, we cannot give you this loan.")
else:
    if credit >= 4:
        if income >= 7 or down_pay >= 7:
            print("You get a loan!")
        elif income >= 4 and down_pay >= 4:
            print("You get a loan!")
        else:
            print("Sorry, we can't give you this loan.")
    else:
        print("Sorry, we can't give you this loan.")