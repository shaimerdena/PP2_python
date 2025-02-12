# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even(n):
    value = 0
    while value <= n:
        if value%2==0:
            yield value
        value += 1

n = int(input())
it = even(n)

print(",".join(map(str,it)))