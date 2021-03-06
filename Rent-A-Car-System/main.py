from RentSystem import RentSystem
from Vehicle import Vehicle
from Customer import Customer
from RentSystemProxy import RentSystemProxy

if __name__ == '__main__':
    rent_system = RentSystem()
    # cars = rent_system.cars
    # # for car in cars:
    # #     print(f"{car} ::: {cars[car]}")
    #
    # car2 = Vehicle("BMW", "e60", 3.0, "STZ4234DHFD6", 3.00, 40.00, 200.00)
    # car3 = Vehicle("AUDI", "A4", 3.0, "TDZ3234DDAS4", 3.00, 40.00, 200.00)
    # car4 = Vehicle("AUDI", "A4", 3.0, "1DZ3234DDAS4", 3.00, 40.00, 200.00)
    # car5 = Vehicle("AUDI", "A4", 3.0, "2DZ3234DDAS4", 3.00, 40.00, 200.00)
    # # # print(car3.__str__())
    # # # print(car3)
    # # rent_system.rent_a_vehicle(car3, "days", 3)
    # # rent_system.rent_a_vehicle(car3, "days", 3)
    #
    gosho = Customer("Gosho")
    gosho.list_cars()
    gosho.rent_week("FDA4234DDAS9",1)
    gosho.rent_week("STZ4234DHFD6",1)
    gosho.rent_week("1DZ3234DDAS4",1)
    gosho.rent_week("2DZ3234DDAS4", 1)
    gosho.rent_week("2DZ3234DDAS4", 1)
    gosho.checkout()
    # gosho.rent_week(car2,4)
    # gosho.list_cars()
    #
    # a = "ASD"
    # print(a.capitalize())
    # print(rent_system.get_vehicle("STZ4234DHFD6").__str__())
    #print(rent_system.rent_a_vehicle("FDA4234DDAS9", "hours", 1))

