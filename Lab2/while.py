i = 1
while i < 6:
  print(i, end = " ")
  i += 1
print()

print("---------------------------------")

#break
i = 1
while i < 6:
  print(i, end = " ")
  if i == 3:
    break
  i += 1
print()

print("--------------------------------")

#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i, end = " ")
print()

print("----------------------------------")
#else
i = 1
while i < 6:
  print(i, end=" ")
  i += 1
else:
  print()
  print("i is no longer less than 6")