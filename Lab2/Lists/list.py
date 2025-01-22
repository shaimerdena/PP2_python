thislist = ["apple", "banana", "cherry", "apple", "cherry"]
list1 = ["abc", 34, True, 40, "male"]
print(thislist)
print(len(thislist))
print(type(list1))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.