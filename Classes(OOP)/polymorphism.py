# Polymorphism: word means many forms. 
# One command that works with different kinds of objects and classes, where each knows how to do that command its own way. 

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Cow:
    def speak(self):
        print("Moo!")

animals = [Dog(), Cat(), Cow()]

for x in animals:
    x.speak()