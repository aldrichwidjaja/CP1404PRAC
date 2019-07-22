x = int(input("Enter X number: "))
y = int(input("Enter Y number: "))

choice = input("""
A) Show even numbers
B) Show Odd numbers
C) Show Squares 
D) Exit""").upper()

while choice !="D":
    if choice == "A":
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end="|")
        choice = input("""
A) Show even numbers
B) Show Odd numbers
C) Show Squares 
D) Exit""").upper()
    elif choice == "B":
        for i in range(x, y+1):
            if i % 2 == 1:
                print(i, end="|")
        choice = input("""
A) Show even numbers
B) Show Odd numbers
C) Show Squares 
D) Exit""").upper()
    elif choice == "C":
        for i in range(x, y):
            square = i**2
            print(square, end="|")
        choice = input("""
A) Show even numbers
B) Show Odd numbers
C) Show Squares 
D) Exit""").upper()
    else:
        print("Invalid Option")
        choice = input("""
A) Show even numbers
B) Show Odd numbers
C) Show Squares 
D) Exit""").upper()