#password_manager.py
#create and display password for the user
#S.Amichand, Feb 22
import sys 

# Variables and Lists I will use
name = ""
age = ""
user = ""
password = ""
member = {"user": "sashin", 
          "password": "Helloyou123"}
passentry = ""

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
    global newpassword
    while True:
        newuser = input("Enter a username: \n")
        if newuser == "":
            print("Please enter something")
        elif newuser in member["user"]:
            print("This user already exists, please choose a new one.")
        else:
            break
    while True:
        newpassword = input("Enter a password. The password MUST have 7 letters, 1 captial letter and a number: \n").strip()
        if (any(passreqs.isupper() for passreqs in newpassword)
            and any(passreqs.isdigit() for passreqs in newpassword) and len(newpassword) >= 8) :
            member["password"] = newpassword
            print("Account was created!")
            loggedin() 

# Logging into an existing user. First loops for username, second loop is for the password
def existingacc():
    global e_username
    global e_password
    while True:
        e_username = input("Enter your username: \n")
        if e_username == "":
            print("Please enter something")
        elif e_username in member["user"]: 
            break
        else:
            print("Enter a valid user")
    while True:
        e_password = input("Please enter your password: \n") 
        if e_password in member['password']:
            print("Access granted!")
            loggedin()
        else:
            print("Wrong password")
        #else:
         #   print("Please type a valid password")

def loggedin():
    global entry
    entry = input("If you wish to save a new password, type 'p'. If you want to view your passwords type 'v'. \n")
    if entry == "p":
        enter_password()
    elif entry == "v":
        print(passentry)
    else:
        print("Make sure to only type p")

def enter_password():
    global newpass
    newpass = input("Enter your password you wish to save: \n")
    if newpass == "":
        print("Please type something")
    else:
        print(Password saved, enter a new )

    
    exit()

# INTRODUCTION
# Informs the user about the program
print("Hello there! This program is designed for you to store your passwords and users.\
This is only for people who are 13 or older.")
question()