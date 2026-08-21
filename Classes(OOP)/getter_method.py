# Getter method is used to access private properties 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property

    def get_age(self): # getter method returns private data
        return self.__age

p1 = Person("Kapil", 29)
print(p1.name)
print(p1.get_age()) # data accessed 