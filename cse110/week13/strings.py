"""
File: strings.py
Author: Jonathan Wright

Purpose: basic function use.
"""

message = input(f"What is your message? ")

def display_normal():
    print(message.capitalize())

def display_upper():
    print(message.upper())

def display_lower():
    print(message.lower())

display_normal()
display_upper()
display_lower()
