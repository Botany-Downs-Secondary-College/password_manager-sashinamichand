#password_manager.py
#create and display password for the user
#S.Amichand, Feb 22
import sys

# Informs the user about the program
print("Hello there! This program is designed for you to store your passwords and users.\
This is only for people who are 13 or older.")

# Asks the user their age and name
def question():
    while True:
        name = input("What is your name?\n")
        age = float(input("How old are you?\n"))
        if age > 13:
            print("Sorry you are too young.")
            sys.exit()
        else:
            print("You are old enough {}" .format(name))
            global login
            login = input("{} Do you have an account or do you wish to create one? If you wish to create one type 1, if you wish to log in an existing one, type 2:\n"))


# Asks if the user wishes to log in or create an account
