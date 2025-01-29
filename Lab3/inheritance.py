#creating a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("Ayau", "Shaimerden")
x.printname()



# creating a child class
class Student(Person):
    def __init__(self, fname, lname, id, year):
        Person.__init__(self, fname, lname)     #can use super() function:  super().__init__(self, fname, lname)
        self.identification = id
        self.graduation_year = year
    def welcome(self):
        print("Welcome,", self.firstname, self.lastname, "to the class of", self.graduation_year)
y = Student("Aru","Adilkhan", 65116, 2025)
y.welcome()