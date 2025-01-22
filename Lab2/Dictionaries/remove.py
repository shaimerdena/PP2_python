thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#pop():  removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

#popitem(): method removes the last inserted item
thisdict.popitem()
print(thisdict)

#del: removes the item with the specified key name
#The del keyword can also delete the dictionary completely
del thisdict["brand"]
print(thisdict)

#clear(): method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


