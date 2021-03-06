from RentSystem import RentSystem
from Vehicle import Vehicle


class RentSystemProxy:
    def __init__(self):
        self.__rent_system = RentSystem()
        self.rented_vehicles_count = 0
        self.bill = 0

    def get_available_vehicles(self):
        vehicles = self.__rent_system.get_available_vehicles()
        for vehicle in vehicles:
            print(vehicle.__str__())

    def rent_hour(self, license_plate, period):
        cost = self.__rent_system.rent_a_vehicle(license_plate, "hours", period)
        self.__check_rent_status(self, cost, license_plate, "hours", period)
        self.bill += cost

    def rent_day(self, license_plate, period):
        cost = self.__rent_system.rent_a_vehicle(license_plate, "days", period)
        self.__check_rent_status(self, cost, license_plate, "days", period)
        self.bill += cost

    def rent_week(self, license_plate, period):
        cost = self.__rent_system.rent_a_vehicle(license_plate, "weeks", period)
        self.__check_rent_status(self, cost, license_plate, "weeks", period)
        self.bill += cost

    def checkout(self):
        if self.rented_vehicles_count > 3:
            self.bill = self.bill * 0.7

        print(f"Your total cost is {self.bill}")

        self.bill = 0
        self.rented_vehicles_count = 0

    @staticmethod
    def __check_rent_status(self, cost, license_plate, type_of_rent, period):
        if cost > 0:
            self.rented_vehicles_count += 1
            vehicle = self.__rent_system.get_vehicle(license_plate)
            print(f"You successfully rented {vehicle.brand} {vehicle.model} for {period} {type_of_rent}."
                  f"\n This will cost {cost} $")
        else:
            print("This car is unavailable")
