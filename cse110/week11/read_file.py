"""
File: read_file.py
Author: Jonathan Wright

Purpose: Read a file.
"""

with open("books.txt") as bfile:
    for line in bfile:
        print(line.strip())