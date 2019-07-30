import random
import re

while True:
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    p = "".join(random.sample(s, passlen))
    is_valid = False

    if (len(p)<6 or len(p)>12):
        print("Not Valid! Total characters should be between 6 and 12")
        print("Password is invalid: ", p)
        continue
    elif not re.search("[A-Z]",p):
        print("Not valid! It should contain one letter between A-Z")
        print("Password is invalid: ", p)
        continue
    elif not re.search("[a-z]", p):
        print("Not valid! It should contain one letter between a-z")
        print("Password is invalid: ", p)
        continue
    elif not re.search("[1-9]", p):
        print("Not valid! It should contain one number between 1-9")
        print("Password is invalid: ", p)
        continue
    elif not re.search("[@!&+_*^$#&]", p):
        print("Not valid! It should contain special characters")
        print("Password is invalid: ", p)
        continue
    elif re.search("[\s]", p):
        print("Not valid! It should not contain any space")
        print("Password is invalid: ", p)
        continue
    else:
        is_valid = True
        break

if(is_valid):
    print("Password is valid: ", p)
