# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#lambda functions
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)       #a function that always doubles the number you send in

print(mydoubler(11))