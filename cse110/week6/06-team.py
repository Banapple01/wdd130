"""
File: team.py
Author: the dream team 

Purpose: should you get to ride?
"""

fr_age = int(input("What is the age of the first rider? "))
fr_height = int(input("What is the height of the first rider? "))

if(fr_height >= 36):
    sr_yn = input("Is there a second rider (yes/no)? ").lower()
    if(12 <= fr_age < 18):
        gp = input("Do you have a golden passport? ").lower()
        if(gp == "yes"):
            fr_age = 18
    if(sr_yn == "yes"):
        sr_age = int(input("What is the age of the second rider? "))
        sr_height = int(input("What is the height of the second rider? "))
        if(12 <= sr_age < 18):
            gp = input("Do you have a golden passport? ").lower()
            if(gp == "yes"):
                sr_age = 18
        if(sr_height >= 36):
            if(sr_age >= 18 or fr_age >= 18):
                print("Yay! You may ride.")
            elif(sr_age >= 12 and fr_age >= 12 and sr_height >= 52 and fr_height >= 52):
                print("Yay! You may ride. line 32")
            elif(sr_age >= 16 and fr_age >= 14 or sr_age >= 14 and fr_age >= 16):
                print("Yay! You may ride. line 30")
            else:
                print("Sorry, you may not ride! line 34")
        else:
            print("Sorry, you may not ride! line 36")
    else:
        if(fr_age >= 18 and fr_height >= 62):
            print("Yay! You may ride. line 39")
        else:
            print("Sorry, you may not ride! line 41")
else:
    print("Sorry, you may not ride! line 43")