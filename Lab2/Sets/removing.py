#remove method: if the item to remove doesn't exist, then function will raise an error
thisset = {"apple", "banana", "cherry", "kiwi", "orange"}

thisset.remove("banana")

print(thisset)

#discard method: If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("orange")

print(thisset)

#pop method: this method will remove a random item, the method can return a value of deleted value
x = thisset.pop()

print(x)

print(thisset)

#clear method: empties the set
thisset.clear()

print(thisset)

#del method: deletes the set completely
del thisset

# print(thisset)   we cannot print the set, bc it was deleted (raises an error)
