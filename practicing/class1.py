class parent:
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age

class Student(parent):
    def __init__(self, name ="", age = 0, course = 0):
        super().__init__(name, age)
        self.course = course
    def inputting(self):
        self.name = input("Your name: ")
        self.age = int(input("Your age: "))
        self.course = int(input("Your course: "))

    def condition(self):
        if self.age > 20:
            print(self.name.upper())
        if self.age < 20:
            print(self.name.lower())

student = Student()
student.inputting()
student.condition()
