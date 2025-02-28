# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def palindrome(strg):
    if strg == "".join(reversed(strg)): print("Palindrome.")
    else: print("Not palindrome.")

strg = input("Enter a string: ")
palindrome(strg)