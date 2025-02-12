# user name
# class person
# functions 2: 1st letter upper, reverse: name Name, eman
#  min 3

class person:
    def __init__(self, str=''):
        self.str = str

    def upper(self):
        print(self.str[0].upper() + self.str[1:])

    def reverse(self):
        print(self.str[::-1])

str = input()
str = person(str)
str.upper()
str.reverse()
