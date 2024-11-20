# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("The car is driving .")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying .")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing .")

# Polymorphism in action
def demonstrate_movement(vehicle):
    vehicle.move()

# Instantiate objects
car = Car()
plane = Plane()
boat = Boat()

# Use polymorphism
demonstrate_movement(car)    # Output: The car is driving 🚗.
demonstrate_movement(plane)  # Output: The plane is flying ✈️.
demonstrate_movement(boat)   # Output: The boat is sailing 🚢.
