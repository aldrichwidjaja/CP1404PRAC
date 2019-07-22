print("Electricity Bill Estimator 2.0")

tarif = input("Which tariff do you use? A) 11 B) 31").upper()
while tarif != "A" and tarif != "B":
    print("Invalid option")
    tarif = input("Which tariff do you use? A) 11 B) 31")
else:
    if tarif == "A":
        cents = 0.244618
        daily = float(input("Enter Daily use in kWh: "))
        billing = float(input("Enter number of billing days: "))
        print("Estimated bill:", cents*daily*billing)
    elif tarif == "B":
        cents = 0.136928
        daily = float(input("Enter Daily use in kWh: "))
        billing = float(input("Enter number of billing days: "))
        print("Estimated bill:", cents * daily * billing)