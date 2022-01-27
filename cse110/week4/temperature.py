"""
File: temperature.py
Author: Jonathan Wright

Purpose: convert F to C.
"""

fahrenheit = float(input("What is the temperature in Fahrenheit? "))
celsius = (fahrenheit-32)*5/9

print(f"\nThe temperature in Celsius is {celsius:.1f} degrees.")