"""
File: madlib.py
Author: Jonathan Wright

Purpose: mad libs.
"""
print("Please enter the following: \n")
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
verb1.replace(" ", "")
if(verb1[-3:] != "ing"):
    verb1 = verb1 + "ing"

exclamation = input("exclamation: ")

verb2 = input("verb: ")
if(verb2[-3:] == "ing"):
    verb2 = verb2.replace("ing", "")

verb3 = input("verb: ")
if(verb3[-3:] == "ing"):
    verb3 = verb3.replace("ing", "")
# these checks don't guarantee proper spelling but they do fix some plural problems.

print(
f'''\nThe other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family.'''
)