# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Child Classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"


# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())
