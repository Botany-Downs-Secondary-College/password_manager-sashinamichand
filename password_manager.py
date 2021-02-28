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
    while True:
        global login
        login = input("{}, do you have an existing account or do you want to create a new one? If it is a new one type 'n', if an existing account type 'e'.\n".format(name))
        login = login.lower()
        if login == "n":
            newacc()
        elif login == "e":
            existingacc()
        else:
            print("Please type either n or e.")

# Creating a new account
def newacc():
    global newuser
    global newpass
    while True:
        newuser = input("Please enter a username: \n")
        if newuser == "":
            print("Please enter something")
        else:
            user.append(newuser)
            break

    while True:
        newpass = input("Please make a password that is 8 letters long, 1 capital letter and a number. \n")
        if newpass.isnumeric() == False:
            print("Please have a number")
        elif len(newpass) < 8:
            print("Please make sure your password is 8 letters long.")
        elif newpass.upper() == False:
            print("Please have a captial letter")
        else:
            print("good")
            break




# Logging into an existing user. First loops for username, second loop is for the password
def existingacc():
    global e_username
    global e_password
    while True:
        e_username = input("Enter your username: \n")
        if e_username == "":
            print("Please enter something")
        elif e_username in user: 
            break
        else:
            print("Enter a valid user")
    while True:
        e_password = input("Please enter your password: \n") 
        if e_password == "":
            print("Please enter something.")
        elif e_password in password:
            print("Welcome user")
            loggedin()
        else:
            print("Please type a valid password")

def loggedin():
    print("hi")
    exit()

# INTRODUCTION
# Informs the user about the program
print("Hello there! This program is designed for you to store your passwords and users.\
This is only for people who are 13 or older.")
question()