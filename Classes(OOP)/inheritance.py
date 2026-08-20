# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class: The class that is being inherited from (Base Class)

# Child Class: The class that inherits from another class (derived class)

class Animal: # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal): # child class
    pass

d1 = Dog("Buddy")

d1.speak()