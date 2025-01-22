# Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

# a tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# the tuple constructer
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

