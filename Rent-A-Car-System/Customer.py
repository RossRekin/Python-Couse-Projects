from RentSystemProxy import RentSystemProxy
from Vehicle import Vehicle


class Customer(object):

    def __init__(self, name):
        self.name = name
        self.rent_system_proxy = RentSystemProxy()

    def list_cars(self):
        self.rent_system_proxy.get_available_vehicles()

    def rent_hour(self, vehicle, hours):
        self.rent_system_proxy.rent_hour(vehicle, hours)

    def rent_day(self, vehicle, days):
        self.rent_system_proxy.rent_day(vehicle, days)

    def rent_week(self, vehicle, weeks):
        self.rent_system_proxy.rent_week(vehicle, weeks)

    def checkout(self):
        self.rent_system_proxy.checkout()
