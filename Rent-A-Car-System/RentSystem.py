from Vehicle import Vehicle


class RentSystem(object):

    def __init__(self):
        self.vehicles = []
        self.__get_all_vehicles()

    def __get_all_vehicles(self):
        car1 = Vehicle("VW", "Golf", 3.0, "FDA4234DDAS9", 3.00, 40.00, 200.00, True)
        car2 = Vehicle("BMW", "e60", 3.0, "STZ4234DHFD6", 3.00, 40.00, 200.00, True)
        car3 = Vehicle("AUDI", "A4", 3.0, "TDZ3234DDAS4", 3.00, 40.00, 200.00, True)
        car4 = Vehicle("AUDI", "A4", 3.0, "1DZ3234DDAS4", 3.00, 40.00, 200.00, True)
        car5 = Vehicle("AUDI", "A4", 3.0, "2DZ3234DDAS4", 3.00, 40.00, 200.00, True)
        self.vehicles = [car1, car2, car3, car4, car5]

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
        for vehicle in self.vehicles:
            if license_plate == vehicle.license_plate:
                if vehicle.is_available:
                    cost = self.calculate_cost(license_plate, type_of_rent, period)
                    vehicle.is_available = False
                    return cost
                else:
                    return 0

    def get_vehicle(self, license_plate):
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate:
                return vehicle
