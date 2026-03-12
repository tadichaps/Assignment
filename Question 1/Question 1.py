# Base class
class Vehicle:
    # Constructor to initialize vehicle name
    def __init__(self, name):
        self.name = name

    # Method defined in the base class
    def move(self):
        # Default movement behavior
        print(self.name + " moves on the road")


# Subclass Car inheriting from Vehicle
class Car(Vehicle):

    # Overriding the move() method from the base class
    def move(self):
        print(self.name + " drives on four wheels 🚗")


# Subclass Bike inheriting from Vehicle
class Bike(Vehicle):

    # Overriding the move() method from the base class
    def move(self):
        print(self.name + " rides on two wheels 🏍️")


# Creating objects of subclasses
car1 = Car("Toyota")
bike1 = Bike("Yamaha")

# Calling the overridden methods
car1.move()
bike1.move()