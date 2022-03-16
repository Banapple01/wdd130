"""
File: life_expectancy.py
Author: Jonathan Wright

Purpose: Read a file.
"""


# import os
# print(os.listdir())

from logging import exception


with open("cse110/week11/life-expectancy.csv") as le:
    def first_max_min(life):
        # print(le)
        max = 0
        max_country = ""
        max_year = ""
        min = 150
        min_country = ""
        min_year = ""
        i = 0
        for line in life:
            # print(line)
            if(i > 0):
                line = line.strip()
                info = line.split(",")
                if(max < float(info[3])):
                    max = float(info[3])
                    max_country = info[0]
                    max_year = info[2]
                if(min > float(info[3])):
                    min = float(info[3])
                    min_country = info[0]
                    min_year = info[2]
            else: 
                i+=1
        print(f"The overall max life expectancy is: {max} from {max_country} in {max_year}")
        print(f"The overall min life expectancy is: {min} from {min_country} in {min_year}\n")
    first_max_min(le)

    
with open("cse110/week11/life-expectancy.csv") as le:
    def second_max_min(life):
        # print(le)
        max = 0
        max_country = ""
        min = 150
        min_country = ""
        yoi = input("Enter the year of interest: ").lower()
        while int(yoi) < 1000 or int(yoi) > 2030:
            print("Please enter a valid year.")
            yoi = input("Enter the year of interest: ").lower()
        i = 0
        j = 1
        average = 0

        try:
            for line in life:
                # print(line)
                if(i > 0):
                    line = line.strip()
                    info = line.split(",")
                    # print(info[2])
                    if(info[2] == yoi and max < float(info[3])):
                        max = float(info[3])
                        max_country = info[0]
                    if(info[2] == yoi and min > float(info[3])):
                        min = float(info[3])
                        min_country = info[0]
                    if(info[2] == yoi):
                        average+=float(info[3])
                        j+=1
                    # print(j)
                else: 
                    i+=1
        except exception as e:
            print(e)

        average = average/j

        print(f"For the year {yoi}:")
        print(f"The average life expectancy across all countries was {average:.3f}")
        print(f"The max life expectancy was in {max_country} with {max:.3f}")
        print(f"The min life expectancy was in {min_country} with {min:.3f}\n")
    second_max_min(le)
    

with open("cse110/week11/life-expectancy.csv") as le:
    def country_history(life):
        i = 0
        countries = []

        for line in life:
            # print(line)
            if(i > 0):
                line = line.strip()
                info = line.split(",")
                if(countries.__contains__(info[0].lower()) == False):
                    countries.append(info[0].lower())
            else: 
                i+=1

        print(f"Here are your country options: {countries}")
        coi = input("Enter the country of interest: ").lower()
        while not countries.__contains__(coi):
            print("Please enter a valid country.")
            coi = input("Enter the country of interest: ").lower()
        i = 0
        
        with open("cse110/week11/life-expectancy.csv") as le:

            for line in le:
                # print(line)
                if(i > 0):
                    line = line.strip()
                    info = line.split(",")
                    # print(info[0].lower())
                    if(info[0].lower() == coi):
                        print(f"Year: {info[2]} Life Expectancy: {float(info[3]):.3f}")
                else: 
                    i+=1

    country_history(le)
