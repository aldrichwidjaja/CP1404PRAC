import random

linenumbers = 6
minimum = 1
maximum = 45

quickp = int(input("How  many quick picks?"))
while quickp < 0 :
    print("Invalid")
    quickp = int(input("How  many quick picks?"))

for i in range(quickp):
    quick_pick = []
    for j in range(linenumbers):
        number = random.randint(minimum, maximum)
        while number in quick_pick:
            number = random.randint(minimum, maximum)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))