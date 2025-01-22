fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x, end= " ")
print()

#string
for x in "banana":
  print(x, end = " ")
print()

#break
for x in fruits:
  print(x, end = " ")
  if x == "banana":
    break
print()

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x, end = " ")
print()

#range()
for x in range(6):
  print(x, end = " ")
print()

for x in range(2, 6):
  print(x, end = " ")
print()

for x in range(2, 30, 3):
  print(x, end = " ")
print()

#else
for x in range(6):
  print(x, end = " ")
else:
  print()
  print("Finally finished!")

#nested
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y, end=" ")
print()

#pass
for x in [0, 1, 2]:
  pass
