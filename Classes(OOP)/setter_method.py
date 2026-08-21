# setter method is used to change/update value to private property. Also to validate before setting 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

        else:
            print("Enter positive age!")

p1 = Person("Kapil", 29)
print(p1.get_age())
p1.set_age(7)
print(p1.get_age())
