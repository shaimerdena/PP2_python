import math

def volume(rad):
    V = (4/3) * rad**3 * math.pi
    return V

rad = float(input())
print(volume(rad))