# Create a base class Employee with attributes name and salary.
# Create Manager and Developer classes that inherit from Employee and add their own attributes like team_size (for managers) and programming_language (for developers).
# Implement a show_details() method in each class to display relevant information.

class Employee:
    def __init__(self, name="", salary = 0):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name="", salary=0, team_size = 0):
        super().__init__(name, salary)
        self.team = team_size

    def show(self):
        print(f"The manager's name is {self.name}, salary is {self.salary} and team_size is {self.team}")

class Developer(Employee):
    def __init__(self, name="", salary=0, programming_language = ""):
        super().__init__(name, salary)
        self.programming = programming_language

    def show(self):
        print(f"Developer's name is {self.name}, salary is {self.salary} and programming language is {self.programming}")

name = input("A name of a manager: ")
salary = int(input("Salary of the manager: "))
team = int(input("Team size of the developer: "))
manager = Manager(name, salary, team)
manager.show()

name1 = input("A name of a developer: ")
salary1 = int(input("Salary of the developer: "))
team1 = input("Programming language of the manager: ")
developer = Developer(name1, salary1, team1)
developer.show()