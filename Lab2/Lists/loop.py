#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x,  end = " ")
print()

# Loop Through the Index Numbers
for i in range(len(thislist)):
  print(thislist[i], end=" ")
print()

#while loop
i = 0
while i < len(thislist):
  print(thislist[i], end = " ")
  i = i + 1
print()

#Looping Using List Comprehension
[print(x, end = " ") for x in thislist]