#password_manager.py
#create and display password for the user
#S.Amichand, Feb 22
import sys 

# Variables and Lists I will use
name = ""
age = ""
user = ["sashin",]
password = ["Helloyou123", ]

# Asks the user their age and name
def question():
    while True:
        global name
        name = input("What is your name?\n")
        if name == "":
            print("Please type something")
        else:
            break
    while True:      
        try:
            global age
            age = float(input("How old are you?\n").strip())
            if age < 13:
                print("Sorry you are too young.")
                break
            else:
                print("You are old enough {}." .format(name))
                signingIn()
        except ValueError: 
            print("Please only type a number")
          
# LOGGING IN 
# Asks if the user wishes to log in or create an account
def signingIn():
    print("Hi")
    sys.exit()
    
# INTRODUCTION
# Informs the user about the program
print("Hello there! This program is designed for you to store your passwords and users.\
This is only for people who are 13 or older.")
question()