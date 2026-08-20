# Object properties: properties defined inside __init__() belong to each objects.

# Class properties: properties defined outside method belong to class and are shared by all objects.

class Person:
    species = "Human" # class property
    lastname = "regs"
    def __init__(self, name):
        self.name = name

p1 = Person("Kapil")
p2 = Person("Pooja")
p1.age = 29
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
print(p1.age) # adding new attribute to an object

Person.lastname = "Regmi" # modifying class properties
print(p1.lastname)
print(p2.lastname)