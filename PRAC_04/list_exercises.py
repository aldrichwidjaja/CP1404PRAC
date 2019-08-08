numbers = []
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)
print(numbers[0])
print(numbers[4])
print(min(numbers))
print(max(numbers))
print(sum(numbers)/len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
checkuser = str(input("Please input username"))
if (checkuser in usernames):
    print("ACCESS GRANTED")
else:
    checkuser = str(input("ACCESS DENIED"))