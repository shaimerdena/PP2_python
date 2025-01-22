thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#get()
x = thisdict.get("model")
print(x)

#keys(): will return a list of all the keys in the dictionary
x = thisdict.keys()
print(x)                #before the change     

thisdict["color"] = "white"

print(x)                #after the change


#values: will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)                #before the change

thisdict["year"] = 2020
print(x)                #after the change


#items(): will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)


#check if key exists
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")