#remove
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#pop (The pop() method removes the specified index.)
thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

#del
del thislist[0]
print(thislist)

del thislist     #delete the list completely 

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)