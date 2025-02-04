def centigrade(F):
    C = (5 / 9) * (F - 32)
    return C

F = float(input())
print(centigrade(F))
