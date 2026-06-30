# smart_city_transport_system.py

class Vehicle:

    def __init__(self, registration_number, manufacturer, speed):
        self.registration_number = registration_number
        self.manufacturer = manufacturer
        self.speed = speed

    def start_vehicle(self):
        print(self.registration_number, "has started.")

    def stop_vehicle(self):
        print(self.registration_number, "has stopped.")


class Bus(Vehicle):

    def __init__(self, registration_number, manufacturer,
                 speed, route_number, passenger_capacity):

        Vehicle.__init__(
            self,
            registration_number,
            manufacturer,
            speed
        )

        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def display_bus(self):
        print("\nBus Information")
        print("Registration Number:", self.registration_number)
        print("Manufacturer:", self.manufacturer)
        print("Speed:", self.speed)
        print("Route Number:", self.route_number)
        print("Passenger Capacity:", self.passenger_capacity)


class ElectricVehicle:

    def __init__(self, battery_level):
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100
        print("Battery fully charged.")

    def battery_status(self):
        print("Battery Level:", self.battery_level, "%")


class ElectricBus(Bus, ElectricVehicle):

    def __init__(self,
                 registration_number,
                 manufacturer,
                 speed,
                 route_number,
                 passenger_capacity,
                 battery_level):

        Bus.__init__(
            self,
            registration_number,
            manufacturer,
            speed,
            route_number,
            passenger_capacity
        )

        ElectricVehicle.__init__(
            self,
            battery_level
        )

    def display_electric_bus(self):

        self.display_bus()
        self.battery_status()


# Objects

bus1 = Bus(
    "UBA123A",
    "Toyota",
    80,
    "Route 5",
    60
)

electric_bus1 = ElectricBus(
    "UBB456B",
    "BYD",
    70,
    "Route 10",
    50,
    75
)

print("\nNORMAL BUS")
bus1.display_bus()

print("\nELECTRIC BUS")
electric_bus1.display_electric_bus()

electric_bus1.charge()
electric_bus1.battery_status()

print("\nMRO")
print(ElectricBus.mro())