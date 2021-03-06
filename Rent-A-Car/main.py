from models.Customer import Customer


if __name__ == '__main__':
    gosho = Customer("Gosho")
    gosho.list_cars()
    gosho.rent_week("E111111", 1)
    gosho.rent_day("A111111", 2)
    gosho.rent_hour("B111111", 1)
    gosho.rent_day("C111111", 6)
    gosho.rent_week("2111111", 4)  # testing wrong license plate
    gosho.rent_hour("E111111", 1)  # testing unavailable vehicle
    gosho.checkout()



