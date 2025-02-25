# Write a Python program to count the number of lines in a text file.

import os

def counting(file_path):
    fhand = open(file_path, "r")
    count = 0
    for line in fhand:
        count += 1
    print(count)

path = r"C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab6\directory\Ayau.txt"
counting(path)