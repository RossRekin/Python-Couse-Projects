


class CarFactory():
    @staticmethod
    def create_car(typ):
        target_class = typ.capitalize()
        return globals()[target_class]()

