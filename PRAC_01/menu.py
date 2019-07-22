name = input("Please input your name: ")
choice = input("""(H)ello
(G)oodbye
(Q)uit""").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
        choice = input("""(H)ello
(G)oodbye
(Q)uit""").upper()
    elif choice == "G":
        print("Goodbye", name)
        choice = input("""(H)ello
(G)oodbye
(Q)uit""").upper()
    else :
        print("Invalid choice")
        choice = input("""(H)ello
(G)oodbye
(Q)uit""").upper()