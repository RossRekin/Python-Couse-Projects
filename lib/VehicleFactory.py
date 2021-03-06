import json
import os
from models.Vehicle import Vehicle


class VehicleFactory():

    @staticmethod
    def load_vehicles():
        vehicles = []

        with open(os.path.join("data", "data.json"), 'r') as json_file:
            data = json.loads(json_file.read())
            for v in data["vehicles"]:
                vehicles.append(Vehicle(**v))
        return vehicles
