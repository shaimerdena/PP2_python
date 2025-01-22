thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "strawberry"]
print(thislist)
thislist[1] = "cherry"
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)
#inserting a new item
thislist.insert(2, "melon")
print(thislist)
