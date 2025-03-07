# Task: Create a generator that yields numbers from 0 to n with a given step s.

# 🔹 Example Input: n = 20, s = 3
# 🔹 Example Output: 0 3 6 9 12 15 18

def generating(n, s):
    value = 0
    while value <= n:
        yield value
        value += s
    
n = int(input())
s = int(input())

for i in generating(n, s):
    print(i, end = " ")