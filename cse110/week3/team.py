"""
File: week3.py
Author: team

Purpose: find the area
"""
import math

square = float(input("What is the length of a side of the square in centimeters? "))
print(f'The area of the square in centimeters is: {square**2}')
print(f'The area of the square in meters is: {(square**2)/10000}')
print(f'The area of the cube in centimeters is: {square**3}')
print(f'The area of the cube in meters is: {(square**3)/10000}')

rectangle_length = float(input("\nWhat is the length of rectangle in centimeters? "))
rectangle_width = float(input("What is the width of rectangle in centimeters? "))
print(f'The area of the rectangle in centimeters is: {rectangle_length*rectangle_width}')
print(f'The area of the rectangle in meters is: {(rectangle_length*rectangle_width)/10000}')

radius = float(input("What is the radius of the circle in centimeters? "))
print(f'The area of the circle in centimeters is: {radius**2 * math.pi}')
print(f'The area of the circle in meters is: {(radius**2 * math.pi)/10000}')
print(f'The area of the sphere in centimeters is: {(radius**3 * math.pi)*4/3}')
print(f'The area of the sphere in meters is: {((radius**3 * math.pi)*4/3)/10000}')