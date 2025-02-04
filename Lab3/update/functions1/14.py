import math

def volume(rad):
    V = (4/3) * rad**3 * math.pi
    return V

rad = float(input())
print(volume(rad))

def area(rad):
    A = 4 * math.pi * rad**2
    return A

print(area(rad))