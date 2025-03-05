#  Task: Write a generator that yields numbers divisible by both 5 and 7 in the range from 0 to n.

# 🔹 Example Input: 50
# 🔹 Example Output: 0 35

def five_seven(n):
    value = 0
    while value < n:
        if value % 5 == 0 and value % 7 == 0:
            yield value
        value += 1

n = int(input())

print(" ".join(map(str, five_seven(n))))