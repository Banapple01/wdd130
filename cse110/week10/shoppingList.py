"""
File: shoppingList.py
Author: Jonathan Wright

Purpose: Go shopping.
"""

s = ""
items = []

while s != "quit":
    s = input("Please enter the items of the shopping list (type: quit to finish): ").lower()
    if s != "quit":
        items.append(s)

print("\nThe shopping list is: ")
for item in items:
    print(f"{item.title()}")

def indexes():
    print("\nThe shopping list with idexes is: ")
    for i in range(len(items)):
        item = items[i]
        print(f"{i}. {item.title()}")
indexes()

change = int(input("Which item would you like to change? "))
items[change] = input("What is the new item? ").lower()

indexes()