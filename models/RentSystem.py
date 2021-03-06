from lib.VehicleFactory import VehicleFactory


class RentSystem(object):

    def __init__(self):
        self.vehicles = []
        self.__get_all_vehicles()

    def get_vehicle(self, license_plate):
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate:
                return vehicle
        return None

    def __get_all_vehicles(self):
        self.vehicles = VehicleFactory.load_vehicles()

    def get_available_vehicles(self):
        available_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.is_available:
                available_vehicles.append(vehicle)
        return available_vehicles

    def calculate_cost(self, license_plate, type_of_rent, period):
        vehicle = self.get_vehicle(license_plate)
        if type_of_rent == "hours":
            return vehicle.cost_per_hour * period
        if type_of_rent == "days":
            return vehicle.cost_per_day * period
        if type_of_rent == "weeks":
            return vehicle.cost_per_week * period

    def rent_a_vehicle(self, license_plate, type_of_rent, period):
        vehicle = self.get_vehicle(license_plate)
        if vehicle:
            if vehicle.is_available:
                cost = self.calculate_cost(license_plate, type_of_rent, period)
                vehicle.is_available = False
                return cost
            else:
                return 0
        else:
            return -1
