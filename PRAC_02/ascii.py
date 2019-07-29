input1 = str(input("Hello, Please input any alphabet"))
if (input1 >='a' and input1 <= 'z') or (input1 >='A' and input1 <= 'Z'):
    print("ASCII Code for", input1, "is", ord(input1))
else:
    print("Invalid input! please input only alphabet")
    input1 = input("Hello, Please input any alphabet")
    print("ASCII Code for", input1, "is", ord(input1))

input2 = int(input("Now, Please input any Number between 33-127"))
if input2 <= 33 or input2 >= 127:
    print("Invalid input! Please input only numbers between 33-127")
    input2 =int(input("Now, Please input any Number between 33-127"))
    print("The character for", input2, "is", chr(input2))
else:
    print("The character for", input2, "is", chr(input2))
