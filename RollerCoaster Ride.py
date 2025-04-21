#import pandas as pd
print("--Wlecom to the rollercoster ride--")
height = int(input("Please enter your height : "))
age = int(input("Please enter your age : "))
ticket = 0

if height > 120:
    print("You can ride ")
    if age<12:
        ticket = 5
        print("Child ticket price {}$".format(ticket))
    elif age <18:
        ticket = 7
        print("Youth ticket price {}$".format(ticket))
    elif age >45 and age <55:
        print('You are in your midlife its wonderfull to have you here your ticket is free enjoy the ride ')
    else:
        ticket = 12
        print("Adult ticket price is {}$".format(ticket))
    wants_phot = (input("Do you want a photo type 'Y' for yes, type 'N for no' "))
    if wants_phot == 'Y':
        ticket = ticket + 3
    print("Your total bill is {}$".format(ticket))
else:
    print("You can not ride ")
