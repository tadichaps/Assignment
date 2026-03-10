from abc import ABC, abstractmethod
import json


# -----------------------------
# Abstract Base Class: Drone
# -----------------------------
class Drone(ABC):
    def __init__(self, drone_id, battery_level=100, temperature=25):
        self.drone_id = drone_id

        # Encapsulation: private attributes
        self.__battery_level = battery_level  # Strongly private (name mangling)
        self._internal_temperature = temperature  # Protected (internal use)

    # Read-only property for battery level
    @property
    def battery_level(self):
        """Read-only access to battery level"""
        return self.__battery_level

    def update_battery(self, consumption):
        """
        Concrete method to reduce battery level.
        Prevents battery from going below 0.
        """
        if consumption < 0:
            raise ValueError("Consumption must be positive")

        self.__battery_level = max(0, self.__battery_level - consumption)

    @abstractmethod
    def Maps(self, destination):
        """
        Abstract navigation method.
        Must be implemented by subclasses.
        """
        pass

    def serialize_state(self, filename):
        """
        Serialize current drone state into a JSON file.
        """
        state = {
            "drone_id": self.drone_id,
            "battery_level": self.__battery_level,
            "internal_temperature": self._internal_temperature,
            "type": self.__class__.__name__
        }

        with open(filename, "w") as file:
            json.dump(state, file, indent=4)

        print(f"Drone state saved to {filename}")

    @classmethod
    def reboot(cls, filename):
        """
        Class method to reboot drone from saved JSON file.
        """
        with open(filename, "r") as file:
            state = json.load(file)

        # Create new instance with saved state
        drone = cls(
            drone_id=state["drone_id"],
            battery_level=state["battery_level"],
            temperature=state["internal_temperature"]
        )

        print(f"Drone {drone.drone_id} successfully rebooted.")
        return drone


# -----------------------------
# Modular Sensor System
# -----------------------------
class Lidar:
    def scan(self):
        return "Scanning environment using LIDAR..."


class GPS:
    def get_location(self):
        return "Fetching coordinates via GPS..."


# -----------------------------
# Subclass: DeliveryDrone
# -----------------------------
class DeliveryDrone(Drone):
    def __init__(self, drone_id, battery_level=100, temperature=25):
        super().__init__(drone_id, battery_level, temperature)
        self.sensors = []  # Modular sensor system

    def add_sensor(self, sensor):
        """
        Inject sensor dependency at runtime.
        """
        self.sensors.append(sensor)

    def Maps(self, destination):
        """
        Overridden navigation logic.
        Uses injected sensors for smart routing.
        """
        print(f"DeliveryDrone {self.drone_id} navigating to {destination}.")

        for sensor in self.sensors:
            if hasattr(sensor, "scan"):
                print(sensor.scan())
            if hasattr(sensor, "get_location"):
                print(sensor.get_location())

        self.update_battery(10)  # simulate energy usage
        print("Navigation complete.")


# -----------------------------
# Simulation Example
# -----------------------------
if __name__ == "__main__":
    # Create delivery drone
    drone1 = DeliveryDrone("DR-101")

    # Inject sensors dynamically
    drone1.add_sensor(Lidar())
    drone1.add_sensor(GPS())

    # Perform navigation
    drone1.Maps("Central Warehouse")

    print("Battery Level:", drone1.battery_level)

    # Serialize state to file
    drone1.serialize_state("drone_state.json")

    # Reboot drone from file
    rebooted_drone = DeliveryDrone.reboot("drone_state.json")
    print("Rebooted Drone Battery:", rebooted_drone.battery_level)
