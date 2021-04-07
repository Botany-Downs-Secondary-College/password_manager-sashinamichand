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
app = ["Codeavengers", ]
userentry = ["sashin123",]
passentry = ["hi",]

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
        elif newuser in member.values():
            print("This user already exists, please choose a new one.")
        else:
            member["user"] = newuser
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

# Asks the user what they what to do or if they wish to view their passwords and the user can also exit
def loggedin():
    while True:
        global choice
        choice = input("If you wish to save a new password, type 'p'. If you want to view your passwords type 'v'. Lastly if you are done type 'e'. \n")
        if choice == "p":
            enter_password()
        elif choice == "v":
            print("The app names are: {}. The user for them are: {} The password for them are: {}." .format(app, userentry, passentry))
        elif choice == "e":
            exit()
        else:
            print("Make sure to only type p")

# A loop that allows the user to enter their passwords
def enter_password():
    while True:
        global appuser
        global appname
        global appPass
        while True: 
            appname = input("Enter the apps name you wish to save, if you are finished type 'f': \n")
            if appname == "":
              print("Please type something")
            elif appname ==  "f":
                loggedin()
            else:
                app.append(appname)
                break
        while True:
            appuser = input("Enter the user for the app you wish to save, and press 'f' if you are done: \n")
            if appuser == "":
              print("Please type something")
            else:
                userentry.append(appuser)
                break
        while True:
            appPass = input("Enter your password you wish to save, and press 'f' if you are done: \n")
            if appPass == "":
                print("Please type something")
            else:
                passentry.append(appPass)
                print("Password saved, enter any more passwords you wish." )    
                enter_password()
                
# INTRODUCTION
# Informs the user about the program
print("Hello there! This program is designed for you to store your passwords and users.\
This is only for people who are 13 or older.")
question()