thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict["year"] = 2018
print(thisdict)

#update(): will update the dictionary with the items from the given argument.
thisdict.update({"year": 2020})
print(thisdict)
