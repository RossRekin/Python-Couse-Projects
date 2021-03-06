from models.RentSystem import RentSystem


class RentSystemProxy:
    def __init__(self):
        self.__rent_system = RentSystem()
        self.rented_vehicles_count = 0
        self.bill = 0

    def get_available_vehicles(self):
        vehicles = self.__rent_system.get_available_vehicles()
        for vehicle in vehicles:
            print(vehicle.__str__())

    def __add_to_cart(self, license_plate, type_of_rent, period):
        cost = self.__rent_system.rent_a_vehicle(license_plate, type_of_rent, period)
        self.__check_rent_status(self, cost, license_plate, type_of_rent, period)
        if cost > 0:
            self.bill += cost

    def rent_hour(self, license_plate, period):
        self.__add_to_cart(license_plate, "hours", period)

    def rent_day(self, license_plate, period):
        self.__add_to_cart(license_plate, "days", period)

    def rent_week(self, license_plate, period):
        self.__add_to_cart(license_plate, "weeks", period)

    def checkout(self):
        if self.rented_vehicles_count > 3:
            self.bill = self.bill * 0.7
            print("Since you rented more than 3 cars, you will get a 30% discount!")
        print(f"Your total cost is {self.bill} $")

        self.bill = 0
        self.rented_vehicles_count = 0

    @staticmethod
    def __check_rent_status(self, cost, license_plate, type_of_rent, period):
        if cost > 0:
            self.rented_vehicles_count += 1
            vehicle = self.__rent_system.get_vehicle(license_plate)
            print(f"You successfully rented {vehicle.brand} {vehicle.model} for {period} {type_of_rent}."
                  f"\n This will cost {cost} $")
        elif cost == 0:
            print("This vehicle is unavailable")
        elif cost == -1:
            print("Vehicle not found")
