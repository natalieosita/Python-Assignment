# Base class
class Vehicle:
    def move(self):
        pass  # Placeholder for subclasses 

# Derived class for Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Derived class for Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Derived class for Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Derived class for Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

# Testing Polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]
for vehicle in vehicles:
    print(vehicle.move())