"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of monthcount."""
    incomes = []
    monthcount = int(input("How many months? "))

    for month in range(1, monthcount + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    printtotal(incomes,monthcount)

def printtotal(incomes,monthcount):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, monthcount + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()
