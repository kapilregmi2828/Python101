class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our Python Class.")

p1 = Person("Kapil")
p1.welcome()