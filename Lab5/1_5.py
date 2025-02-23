import re

#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

print("1) ", end = "")
with open("example", "r") as file:
        data = file.read()
        print(re.findall(r"\ba+b*\b", data))

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

print("2) ", end = "")
with open("example", "r") as file:
        data = file.read()
        print(re.findall(r"\bab{2,3}\b", data))

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.

print("3) ", end = "")
with open("example", "r") as file:
        data = file.read()
        print(re.findall(r"[a-z]+_[a-z]+", data))

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.

print("4) ", end = "")
with open("example", "r") as file:
        data = file.read()
        print(re.findall(r"\b[A-Z][a-z]+\b", data))

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

print("5) ", end = "")
with open("example", "r") as file:
        data = file.read()
        print(re.findall(r"\ba.+b\b", data))