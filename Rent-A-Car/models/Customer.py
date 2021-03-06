from models.RentSystemProxy import RentSystemProxy



class Customer(object):

    def __init__(self, name):
        self.name = name
        self.rent_system_proxy = RentSystemProxy()

    def list_cars(self):
        self.rent_system_proxy.get_available_vehicles()

    def rent_hour(self, license_plate, hours):
        self.rent_system_proxy.rent_hour(license_plate, hours)

    def rent_day(self, license_plate, days):
        self.rent_system_proxy.rent_day(license_plate, days)

    def rent_week(self, license_plate, weeks):
        self.rent_system_proxy.rent_week(license_plate, weeks)

    def checkout(self):
        self.rent_system_proxy.checkout()
