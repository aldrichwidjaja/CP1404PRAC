from car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print("{}, {}, {}".format(my_car.name, my_car.fuel, my_car.odometer))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)

    print(limo)

main()
