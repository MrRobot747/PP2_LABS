class StringManipulator:
    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

obj = StringManipulator()
obj.getString()
obj.printString()
