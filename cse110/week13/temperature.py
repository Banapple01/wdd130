"""
File: temperature.py
Author: Jonathan Wright

Purpose: what's the temperature?
"""

def temperature_func():
    temp = float(input("What's the temperature? "))
    corf = input("Fahrenheit or Celsius (F/C)? ").lower()
    if corf == "c":
        temp = temp * (9/5) + 32
        # temp = ((temp - 32) / 1.8000)


    v = 5.0

    while v < 65.0:
        windchill = 35.74 + (0.6215*temp) - (35.75*(v**0.16)) + (0.4275*temp*(v**0.16))
        print(f"At temperature {temp:.2f}F, and wind speed {v:.0f} mph, the windchill is: {windchill:.2f}F")
        v+=5.0

temperature_func()
