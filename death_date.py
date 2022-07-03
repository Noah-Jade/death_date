from random import *
from datetime import date


name = input("What is your name? ")
birth = input("What year were you born? ")
question = input("Would you like to know when you'll die? Enter Yes or No... ")

today = date.today()


def death_date():
    return randint(1, 60) + today.year


if question == "Yes":
    print("You will perish in " + str(death_date()) + ", " + name + ". Rip :(.")
else:
    print("Your fate remains a mystery " + name + ".")

input("Press [Enter] to continue.")

# def age():
#    return today.year - int(birth)

