class String:
    def getString(self):
        self.name = input()
    def printString(self):
        print(self.name.upper())
    
mystring = String()
mystring.getString()
mystring.printString()
    