thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict["color"] = "black"
print(thisdict)

#update(): will update the dictionary with the items from a given argument. 
#If the item does not exist, the item will be added.
thisdict.update({"horsepower": 460})
print(thisdict)