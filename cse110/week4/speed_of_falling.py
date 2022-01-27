"""
File: temperature.py
Author: Jonathan Wright

Purpose: Find the speed of a falling object.
"""

gravity_m = 9.80665
gravity_f = 32.17405

time = float(input("How long did it take for the ball to fall? "))
distance = input("Feet or Meters? ")
if(distance == 'feet' or distance == 'Feet'):
    speed = gravity_f * time;
    print(f"The speed of the ball is {speed:.3f} feet per second.")
elif(distance == 'meters' or distance == 'Meters'):
    speed = gravity_m * time;
    print(f"The speed of the ball is {speed:.3f} meters per second.")

