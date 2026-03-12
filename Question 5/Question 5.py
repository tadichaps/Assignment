# Base class
class SmartDevice:
    def __init__(self, name):
        self.name = name

    def reset(self):
        """
        Default reset behavior for a generic smart device.
        This method can be overridden by subclasses.
        """
        print(f"{self.name}: Performing standard device reset...")


# Subclass inheriting from SmartDevice
class SmartLight(SmartDevice):
    def reset(self):
        """
        Overridden reset method for SmartLight.
        Provides specialized reset behavior.
        """
        print(f"{self.name}: Resetting light settings and brightness levels...")


# Function demonstrating polymorphism
def reset_all_devices(devices_list):
    """
    Accepts a list of SmartDevice objects.
    Calls the reset() method on each object.

    Due to polymorphism, the correct reset()
    method is executed depending on the object type.
    """
    for device in devices_list:
        device.reset()  # Polymorphic behavior occurs here


# Create objects
device1 = SmartDevice("Smart Thermostat")
light1 = SmartLight("Living Room Light")
light2 = SmartLight("Bedroom Light")

# Store different object types in the same list
devices = [device1, light1, light2]

# Call the function
reset_all_devices(devices)