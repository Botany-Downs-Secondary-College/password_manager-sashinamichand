#password_manager.py
#create and display password for the user
#S.Amichand, Feb 22
import sys 

# Variables and Lists I will use
name = ""
age = ""
login = ""
user = ""
password = ""
i = 0
member = {"user": "sashin", 
          "password": "Helloyou123"}
app = ["Codeavengers", ]
userentry = ["sashin123",]
passentry = ["hi",]

# Checks to make sure user is of age and that they typed their name
def check(name, age):
    if name == "":
        print("Please type a name")
        return()
    if age < 13:
        print("Sorry you are too young.")
        exit()
    else:
        print("You are old enough {}." .format(name))
        return()

# Checks to make sure new account meets the requirements
def newacc(newuser, newpassword):
    global tempPass
    tempPass = newpassword.lower()

    if newuser in member.values():
        print("This user already exists, please choose a new one.")
        return()
    elif newuser or newpassword == "":
        print("Please type something")
        return()
    elif newpassword.isalnum() == False:
        print("Password should contain atleast one number")
        return()
    elif len(newpassword) < 8:
        print("Password should contains atleast 8 letters .")
        return()
    elif tempPass == newpassword:
        print("Password should contain a captial letter.")
        return()



    else:
        member["password"] = newpassword
        member["user"] = newuser
        print("Account was created!")
        return() 
  
        
# Checks to make sure the existing username and password is correct
def existingacc(e_username, e_password, i):
    if e_username or e_password == "":
        print("Enter a valid user/password")
        return()
    elif e_username in member["user"]: 
        print("This username is already in use, choose another one please.")
        return()
    elif e_password in member['password']:
            print("Access granted {}!" .format(name))
            i += 1
            return()
    else:
        print("Wrong password")       

# Checks to see if what the user entered for their app account details is correct
def savepass(appName, appUser, appPass):
    if appName or appUser or appPass == "":
        print("Please type something")
        return()
    else:
        app.append(appName)
        userentry.append(appUser)
        passentry.append(appPass)
        return()        

# Main Routine
# Informs the user about the program
print("Hello there! This program is designed for you to store your passwords and users.\
This is only for people who are 13 or older.")

# Loop for asking the user what their name and age is
while True:
    try:
        name = input("What is your name?\n")
        age = float(input("How old are you?\n").strip())
        check(name, age)
        break
    except ValueError: 
        print("Please enter a number/name")

# Loop to see if the user wishs to login or create an account     
while True:       
    login = input("{}, do you have an existing account or do you want to create a new one? If it is a new one type 'n', if an existing account type 'e'.\n" .format(name))
    login = login.lower()
    if login == "":
        print("Please type either e or n.")
    else:
        break

while True:
    if login == "n":
        newuser = input("Enter a username: \n")
        newpassword = input("Enter a password. The password MUST have 7 letters, 1 captial letter and a number: \n").strip()
        newacc(newuser, newpassword)
        break

while True:
    if login == "e":
        e_username = input("Enter your username: \n")
        e_password = input("Please enter your password: \n") 
        existingacc(e_username, e_password, )
        break

# Asks the user what they want to do
while True:
    choice = input("If you wish to save a new password, type 'p'. If you want to view your passwords type 'v'. Lastly if you are done type 'e'. \n")
    if choice == "":
        print("Please only type either v, e or p.")
    else:
        break
if choice == "p":
    while True:
        appName = input("Enter the app name you wish to save, whenever you are finished inputting your app account details type 'f': \n")
        appUser = input("Enter the username for the app: \n")
        appPass = input("Enter your password : \n")
        savepass(appName, appUser, appPass)
        break
elif choice == "v":
        print("The app names are: {}. The user for them are: {} The password for them are: {}." .format(app, userentry, passentry))
elif choice == "e":
    exit()
else:
    print("Make sure to only type p, v or e. ")