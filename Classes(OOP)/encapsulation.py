# Encapsulation is about protecting data in the class.
# Keep important stuff safely inside and provide simple ways to use it. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private Property

p1 = Person("Kapil", 29)
print(p1.name)
print(p1.__age) # will throw an error because age is not accessed. 