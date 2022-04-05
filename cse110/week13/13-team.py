"""
File: teamRocket.py
Author: Team

Purpose: Areas!
"""

import cmath


def compute_area_square(side):
    return compute_area_rectangle(side,side)

def compute_area_rectangle(side_1,side_2):
    return side_1 * side_2

# Pi * r^2
def compute_area_circle(radius):
    return cmath.pi * radius**2

def compute_area(shape, unit_1, unit_2 = 1):
    if shape == "square":
        print(f"The area of the square is {compute_area_square(unit_1):.2f}")
    
    if shape == "rectangle":
        print(f"The area of the Rectangle is {compute_area_rectangle(unit_1, unit_2):.2f}")
    
    if shape == "circle":
        print(f"The area of the circle is {compute_area_circle(unit_1):.2f}")
    return 

shape = ""

while shape != "rectangle" or shape != "square" or shape != "circle":
    print("Please enter 'rectangle', 'square' or 'circle'.")
    shape = input("What shape do we have? ").lower()

    if shape == "square":
        side = float(input("Give me a side! "))
        print(f"The area of the square is {compute_area_square(side):.2f}")

    if shape == "rectangle":
        side_1 = float(input("Give me side 1! "))
        side_2 = float(input("Give me side 2! "))
        compute_area(shape, side_1, side_2)

    if shape == "circle":
        rad = float(input("Give me a radius! "))
        compute_area(shape, rad)

    if shape == "quit":
        break
