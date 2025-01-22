#add method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#update method:               The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]

thisset.update(tropical)
thisset.update(mylist)

print(thisset)