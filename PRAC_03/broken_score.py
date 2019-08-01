"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def scoree(score):
    if score < 0:
        main = text0
    elif score > 100:
        main = text1
    elif score >= 50 and score<90:
        main = text2
    elif score >= 90:
        main = text3
    elif score < 50:
        main = text4
    return main

text0 = "Invalid Score"
text1 = "Invalid score"
text2 = "Passable"
text3 = "Excellent"
text4 = "Bad"
score = float(input("Enter score: "))
main = scoree(score)
print(main)
