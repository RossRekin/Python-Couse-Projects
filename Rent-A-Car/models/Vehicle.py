class Vehicle(object):
    def __init__(self, brand, model, consumption, license_plate, cost_per_hour, cost_per_day, cost_per_week):
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.license_plate = license_plate
        self.cost_per_hour = cost_per_hour
        self.cost_per_day = cost_per_day
        self.cost_per_week = cost_per_week
        self.is_available = True

    def __str__(self):
        return f"{self.brand} {self.model},{self.license_plate}: \n  Rates => Hour: {self.cost_per_hour}$, Day: {self.cost_per_day}$, " \
               f"Week: {self.cost_per_week}$ \n  Consumption: {self.consumption}"
