thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x, end=" ")
print()

for x in thisdict:
  print(thisdict[x], end=" ")
print()

#keys()
for x in thisdict.keys():
  print(x, end= " ")
print()

#values()
for x in thisdict.values():
  print(x, end = " ")
print()

#items()
for x, y in thisdict.items():
  print(x, y, end = " ")
print()