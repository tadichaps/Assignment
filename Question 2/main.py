# Import required modules
from abc import ABC, abstractmethod
import json


# ------------------------------
# Sensor Classes (Modular System)
# ------------------------------

class Lidar:
    """Example sensor class that could be injected into a drone at runtime"""
    def scan(self):
        return "Scanning surroundings with Lidar"


class GPS:
    """GPS sensor providing location data"""
    def get_location(self):
        return "Current GPS location"


# -------------------------------------
# Abstract Base Class: Drone (Abstraction)
# -------------------------------------

class Drone(ABC):
    """
    Base Drone class defining common drone behavior.
    Demonstrates abstraction and encapsulation.
    """

    def __init__(self, drone_id, battery_level, internal_temperature):
        self.drone_id = drone_id

        # Private attributes (Encapsulation)
        self.__battery_level = battery_level   # double underscore -> strongly private
        self._internal_temperature = internal_temperature  # protected attribute

    # Read-only property for battery level
    @property
    def battery_level(self):
        """Allow read-only access to battery level"""
        return self.__battery_level

    # Concrete method
    def update_battery(self, consumption):
        """
        Reduce battery level based on energy consumption.
        """
        self.__battery_level -= consumption
        if self.__battery_level < 0:
            self.__battery_level = 0

    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def Maps(self, destination):
        """
        Abstract navigation method.
        Each drone type must define its own navigation logic.
        """
        pass

    # -----------------------------
    # Serialize drone state to JSON
    # -----------------------------
    def save_state(self, filename):
        """Save the current drone state to a JSON file"""
        state = {
            "drone_id": self.drone_id,
            "battery_level": self.__battery_level,
            "internal_temperature": self._internal_temperature,
            "type": self.__class__.__name__
        }

        with open(filename, "w") as file:
            json.dump(state, file, indent=4)

        print("Drone state saved to file.")

    # ---------------------------------
    # Reboot drone by loading from JSON
    # ---------------------------------
    @classmethod
    def reboot(cls, filename):
        """Load drone state from a JSON file and recreate the drone object"""
        with open(filename, "r") as file:
            state = json.load(file)

        # Create a new drone instance using saved data
        drone = cls(
            state["drone_id"],
            state["battery_level"],
            state["internal_temperature"]
        )

        print("Drone rebooted from saved state.")
        return drone


# ----------------------------------------
# Subclass: DeliveryDrone (Inheritance)
# ----------------------------------------

class DeliveryDrone(Drone):
    """
    Specialized drone for package delivery.
    Overrides navigation logic and supports modular sensors.
    """

    def __init__(self, drone_id, battery_level, internal_temperature, sensors=None):
        super().__init__(drone_id, battery_level, internal_temperature)

        # Modular sensor system
        # Sensors can be injected dynamically at runtime
        self.sensors = sensors if sensors else []

    # Override navigation method
    def Maps(self, destination):
        """
        Navigation logic for delivery drones.
        Uses available sensors to reach a destination.
        """
        print(f"Drone {self.drone_id} navigating to {destination}")

        for sensor in self.sensors:
            if isinstance(sensor, GPS):
                print(sensor.get_location())

            if isinstance(sensor, Lidar):
                print(sensor.scan())

        print("Optimizing route for delivery...")


# -------------------------
# Example Simulation Usage
# -------------------------

# Create sensor objects
gps = GPS()
lidar = Lidar()

# Inject sensors into drone (Modular design)
drone1 = DeliveryDrone(
    drone_id="DR-101",
    battery_level=100,
    internal_temperature=35,
    sensors=[gps, lidar]
)

# Use drone navigation
drone1.Maps("Warehouse B")

# Update battery
drone1.update_battery(15)
print("Battery level:", drone1.battery_level)

# Save drone state
drone1.save_state("drone_state.json")

# Reboot drone from saved state
rebooted_drone = DeliveryDrone.reboot("drone_state.json")

print("Rebooted Drone Battery:", rebooted_drone.battery_level)