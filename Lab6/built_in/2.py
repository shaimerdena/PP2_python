# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def counting(strg):
    upper_case = len([i for i in strg if i == i.upper()])
    lower_case = len([i for i in strg if i == i.lower()])
    print("The number of upper case letters:", upper_case)
    print("The number of upper case letters:", lower_case)

strg = input("Enter a string: ")
counting(strg)