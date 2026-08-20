class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
c1 = Car("Honda", "Accord")

print(c1.model)
print(c1.brand)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Kapil", 29)
print(p1.age)

p1.age = 28
print(p1.age)

print(p1.name)
del p1.age
print(p1.age)