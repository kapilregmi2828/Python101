# encapsulation is about protecting data inside a class and how it can be accessed outside. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private property

p1 = Person("Kapil", 29)

print(p1.name)
#print(p1.__age) # error since age is not accessed


