"""
File: lists.py
Author: Jonathan Wright

Purpose: make a list of friend names.
"""

friends = []
name = ""

while name != 'end':
    if name != 'end' or name != "":
        friends.append(name.capitalize())
    name = str(input("Type the name of a friend: ")).lower()

print("\nYour friends are: ")
for name in friends:
    print(name)