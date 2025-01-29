# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

#arbitrary arguments, *args
def kid_s(*kids):
  print("The youngest child is " + kids[2])
kid_s("Emil", "Tobias", "Linus")


#keyword arguments, kwargs
def children(child3, child2, child1):
  print("The youngest child is " + child3)
children(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#arbitrary keyword arguments, **kwargs
def kids(**kid):
  print("His last name is " + kid["lname"])
kids(fname = "Tobias", lname = "Refsnes")


#default parameter value
def countries(country = "Norway"):
  print("I am from " + country)
countries("India")
countries()


#Passing a List as an Argument
def fo_od(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
fo_od(fruits)


#positional-only arguments
#1
def pos1(x, /):
  print(x)
pos1(3)
#2
def pos2(x):
  print(x)
pos2(x = 3)


#keyword-only arguments
#1
def key1(*, x):
  print(x)
key1(x = 3)
#2
def key2(x):
  print(x)
key2(3)


#combine positional-only and keyword-only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)