"""
File: team.py
Author: Jonathan Wright

Purpose: id card.
"""
print("Please enter the following information: \n")
first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job = input("Job title: ")
id = input("ID Number: ")
hair = input("Hair Color: ")
eyes = input("Eye Color: ")
month = input("Starting Month: ")
train = input("Advanced Training: ")


print(
f"\nThe ID Card is:\n"
f"----------------------------------------\n"
f"{last.upper()}, {first.capitalize()}\n"
f"{job.title()}\n"
f"ID: {id}\n"

f"{email.lower()}\n"
f"{phone}\n"

f'''
Hair: {hair.capitalize():9}        Eyes: {eyes.capitalize()}
Month: {month.capitalize():10}      Training: {train.capitalize()}
----------------------------------------'''
)