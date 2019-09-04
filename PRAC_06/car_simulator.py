from car import Car

menu = """Menu: 
d) Drive
r) Refuel
q) quit"""

print("Let's drive!")
carname = input("Enter your car name: ")
car = Car(carname, 100)
print(car)
print(menu)
menuchoose = input("Enter your choice: ").lower()
while menuchoose != "q":
    if menuchoose == "d":
        drive_distance = int(input("How many km do you want to drive?"))
        while drive_distance <= 0:
            print("Distance must be >= 0")
            drive_distance = int(input("How many km do you want to drive?"))
        driven_distance = car.drive(drive_distance)
        print("The car drove {}km".format(driven_distance))
        if car.fuel == 0:
            print("and ran out of fuel".format(driven_distance))
        print(menu)
        menuchoose = input("Enter your choice: ").lower()
    elif menuchoose == "r":
        refillfuel = int(input("How many units of fuel do you want to add?"))
        while refillfuel <= 0 :
            print("Fuel amount must be >= 0")
            refillfuel = int(input("How many units of fuel do you want to add?"))
        car.add_fuel(refillfuel)
        print("Added {} units of fuel.".format(refillfuel))
        print(menu)
        menuchoose = input("Enter your choice: ").lower()
    else:
        print("Invalid choice")
        print(car)
        print(menu)
        menuchoose = input("Enter your choice: ").lower()
print("Good bye {}'s driver".format(car.name))

