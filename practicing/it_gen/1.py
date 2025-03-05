# Task: Write a generator that yields prime numbers in the range from 2 to n.

# 🔹 Example Input: 20
# 🔹 Example Output: 2 3 5 7 11 13 17 19

def prime(n):
    value = 2
    while value <= n:
        count = 0
        for i in range(2, value):
            if value%i == 0:
                count += 1
        if count == 0:
            yield value
        value += 1

n = int(input())   

for i in prime(n):
    print(i, end = " ")
print()

print(",".join(map(str, prime(n))))