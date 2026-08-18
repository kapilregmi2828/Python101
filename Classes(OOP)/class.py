# Python is a Object-Oriented language, meaning it allows you to structure you code using classes and objects for better organization and reusability
# Class is a blueprint from which objects are created.
# Object are things made from blueprint (class)
# Attributes are objects features or informations.
# Methods() are things objects can do (actions)
# self means this particular object
# __init__ sets things up when the object is created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello this is", self.name,"." "I am", self.age, "years old.")

p1 = Person("Kapil", 29)
p2 = Person("Pooja", 28)

p1.greet()
p2.greet()