import re

while True:
    user_input = input("Enter a password : ")
    is_valid = False

    if (len(user_input)<6 or len(user_input)>12):
        print("Not Valid! Total characters should be between 6 and 12")
        continue
    elif not re.search("[A-Z]",user_input):
        print("Not valid! It should contain one letter between A-Z")
        continue
    elif not re.search("[a-z]", user_input):
        print("Not valid! It should contain one letter between a-z")
        continue
    elif not re.search("[1-9]", user_input):
        print("Not valid! It should contain one number between 1-9")
        continue
    elif not re.search("[@!&+_*^$#&]", user_input):
        print("Not valid! It should contain special characters")
        continue
    elif re.search("[\s]", user_input):
        print("Not valid! It should not contain any space")
        continue
    else:
        is_valid = True
        break

if(is_valid):
    print("Password is valid: ", user_input)

