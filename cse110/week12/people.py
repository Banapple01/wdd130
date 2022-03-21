"""
File: people.py
Author: Jonathan Wright

Purpose: lists.
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 999
youngest_name = ""

for person in people:
    name_and_age = person.split(" ")
    age = int(name_and_age[1])
    if age < youngest_age:
        youngest_age = age
        youngest_name = name_and_age[0]

print(f"The youngest person in the list is {youngest_name}, who is {youngest_age} years old.")
