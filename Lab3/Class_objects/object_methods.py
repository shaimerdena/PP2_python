class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name, "I am", abc.age)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40   #modifying object properties
p1.myfunc()

del p1.age    #deleting the object properties

del p1        #deleting the object


