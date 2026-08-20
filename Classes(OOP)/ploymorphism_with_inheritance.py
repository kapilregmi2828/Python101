class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Moves!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

c1 = Car("Honda", "Accord")
b1 = Boat("Yamaha", "Touring")
p1 = Plane("Boeing", "747")

for x in (c1, b1, p1):
    print(x.brand)
    print(x.model)
    x.move()