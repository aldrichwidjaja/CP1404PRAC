"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def celsius1(celsius):
    test = celsius * 9.0 / 5 + 32
    return test
def fahrenheit1(fahrenheit):
    test = 5 / 9 * (fahrenheit - 32)
    return test


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius1(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit1(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
