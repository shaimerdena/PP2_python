#changing tuple values, adding a new item, removing items
x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"         #changing
y.append("orange")    #adding
y.remove("apple")

x = tuple(y)

print(x)

#adding tuple to a tuple
y = ("banana",)
x += y

print(x)

del x
# print(x)     #this will raise an error bc the tuple no longer exists