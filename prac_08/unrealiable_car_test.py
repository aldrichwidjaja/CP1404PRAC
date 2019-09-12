from unreliable_car import carreliable

def main():
    reliable_car = carreliable("Mostly reliable", 100, 70)
    not_reliable_car = carreliable("Not reliable", 100, 5)

    for i in range(1,5):
        print("DRIVE {}km:".format(i))
        print("{:12} Drove {:2}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{:12} Drove {:2}km".format(not_reliable_car.name, not_reliable_car.drive(i)))

    print(reliable_car)
    print(not_reliable_car)

main()
