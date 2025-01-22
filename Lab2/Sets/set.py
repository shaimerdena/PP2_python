# Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry", False, True, 0, 1}  #True and 1, False and 0 are are treated as duplicates
print(thisset)
print(len(thisset))
print(type(thisset))

#the set() constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)