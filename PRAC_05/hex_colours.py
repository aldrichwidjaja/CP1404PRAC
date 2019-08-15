color_name = {"ALICEBLUE": "#f0f8ff", "WHITE1": "#F13122", "WHITE2": "#F12T1F2", "WHITE3": "#F141T2", "RED1": "#F14123R", "RED2": "#Y125123T", "BLACK10": "#F1F1F22", "BLACKWHITE": "#F1F122222" }

pickcolor = input("Enter color of choice: ").upper()
while pickcolor !="":
    if pickcolor in color_name:
        print(pickcolor, "is", color_name[pickcolor])
    else:
        print("Invalid choice!")
    pickcolor = input("Enter color of choice: ").upper()
