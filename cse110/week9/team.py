"""
File: lists.py
Author: Jonathan Wright

Purpose: make a list of friend names.
"""

numbers = []
user_num = -1

print("Enter a list of numbers, type 0 when finished.")
while user_num != 0:
    user_num = int(input("Enter number: "))
    if user_num != 0:
        numbers.append(user_num)

sum = 0
largest = -1000
smallest_pos = 1000
i = 0
for number in numbers:
    sum += number
    if number > largest:
        largest = number
    if number < smallest_pos and number >= 0:
        smallest_pos = number
    i += 1

average = sum/i
# print(average)

length = len(numbers)
average = sum/length

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest_pos}")
numbers.sort()
print(f"The sorted list is: {numbers}")

