# Write a Python program that invoke square root function after specific milliseconds

import time
import math

def program(milliseconds, number):
    time.sleep(milliseconds/1000)
    square = math.sqrt(number)
    print(f"Square root {number} of after {milliseconds} miliseconds is {square}")

number = int(input("Enter a number: "))
millisecond = int(input("Enter delay in milliseconds: "))
program(millisecond, number)

