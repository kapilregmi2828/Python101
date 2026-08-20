class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello my name is " + self.name, "and my age is",self.age)

p1 = Person("Kapil", 29)
p1.greet()


