"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        num = int(input("Input integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", num)
