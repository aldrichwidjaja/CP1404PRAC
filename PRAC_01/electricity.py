print("Electricity bill estimator")
cents = float(input("Enter cents per kWh:"))
daily = float(input("Enter daily use in kWh:"))
billing = float(input("Enter number of billing days:"))
print("Estimated Bill", billing*daily*(cents/100))