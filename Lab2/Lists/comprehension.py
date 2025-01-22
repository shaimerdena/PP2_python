# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

# newlist = [x for x in fruits if x != "apple"]

# newlist = [x for x in range(10)]

# newlist = [x for x in range(10) if x < 5]

# newlist = [x.upper() for x in fruits]

# newlist = ['hello' for x in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

#"Return the item if it is not banana, if it is banana return orange".