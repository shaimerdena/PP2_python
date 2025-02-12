# Create a generator that generates the squares of numbers up to some number N.

def square(n):
    value = 1
    while value<=n:
        yield value**2
        value += 1

n = int(input())
it = iter(square(n))
for i in range(n):
    print(next(it), end = " ")